# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2025/2/26 09:47
# @Author  : weizjajj 
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: openai_agent_template.py
import datetime
import json
from queue import Queue
from typing import Any, List, Dict

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable, RunnableConfig

from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.agent.memory.message import Message
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.plan.planner.react_planner.stream_callback import StreamOutPutCallbackHandler, \
    InvokeCallbackHandler, OpenAIProtocolStreamOutPutCallbackHandler

from agentuniverse.agent.template.agent_template import AgentTemplate
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.prompt import Prompt


class OpenAIProtocolTemplate(AgentTemplate):

    def run(self, **kwargs) -> OutputObject:
        """Agent instance running entry.

        Returns:
            OutputObject: Agent execution result
        """
        kwargs = self.parse_openai_agent_input(kwargs)
        output_object = super().run(**kwargs)
        return self.parse_openai_protocol_output(output_object)

    def parse_openai_agent_input(self, agent_input):
        for key in self.openai_protocol_input_keys():
            if key not in agent_input:
                raise ValueError(f"{key} is not in agent input")
        messages = agent_input.get('messages')
        convert_messages = self.convert_message(messages)
        input = messages[-1].get('content')
        agent_input['input'] = input
        if len(convert_messages) > 1:
            agent_input['chat_history'] = convert_messages[0:len(convert_messages) - 1]
        return agent_input

    def openai_protocol_input_keys(self) -> list[str]:
        return [
            'messages', 'stream'
        ]

    def convert_message(self, messages: List[Dict]):
        for message in messages:
            if message.get('role') == 'user':
                message['type'] = 'human'
            elif message.get('role') == 'assistant':
                message['type'] = 'ai'
        return [Message.from_dict(message) for message in messages]

    def parse_openai_protocol_input(self, input_object: InputObject, agent_input: dict) -> dict:
        for key in self.input_keys():
            if input_object.get_data(key):
                agent_input[key] = input_object.get_data(key)
        messages = agent_input.get('messages')
        convert_messages = self.convert_message(messages)
        input = messages[-1].get('content')
        agent_input['input'] = input
        if len(convert_messages) > 1:
            agent_input['chat_history'] = convert_messages[0:len(convert_messages) - 1]
        return agent_input

    def parse_openai_protocol_output(self, output_object: OutputObject) -> OutputObject:
        res = {
            "object": "chat.completion",
            "id": FrameworkContextManager().get_context('trace_id'),
            "created": int(datetime.datetime.now().timestamp()),
            "model": self.agent_model.info.get('name'),
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": output_object.get_data('output')
                    }
                }
            ],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }
        }
        return OutputObject(params=res)

    def add_output_stream(self, output_stream: Queue, agent_output: str) -> None:
        if not output_stream:
            return
        output = {
            "object": "chat.completion.chunk",
            "id": FrameworkContextManager().get_context('trace_id'),
            "created": int(datetime.datetime.now().timestamp()),
            "model": self.agent_model.info.get('name'),
            "choices": [
                {
                    "delta": {
                        "role": "assistant",
                        "content": agent_output
                    },
                    "index": 0,
                }
            ]
        }
        output_stream.put(json.dumps(output))

    def customized_execute(self, input_object: InputObject, agent_input: dict, memory: Memory, llm: LLM, prompt: Prompt,
                           **kwargs) -> dict:
        self.load_memory(memory, agent_input)
        process_llm_token(llm, prompt.as_langchain(), self.agent_model.profile, agent_input)
        chain = prompt.as_langchain() | llm.as_langchain_runnable(
            self.agent_model.llm_params()) | StrOutputParser()
        res = self.invoke_chain(chain, agent_input, input_object, **kwargs)
        self.add_memory(memory, f"Human: {agent_input.get('input')}, AI: {res}", agent_input=agent_input)
        return {**agent_input, 'output': res}

    def _get_run_config(self, input_object: InputObject) -> RunnableConfig:
        config = RunnableConfig()
        callbacks = []
        output_stream = input_object.get_data('output_stream')
        callbacks.append(OpenAIProtocolStreamOutPutCallbackHandler(output_stream, agent_info=self.agent_model.info))
        callbacks.append(InvokeCallbackHandler(source=self.agent_model.info.get('name'),
                                               llm_name=self.agent_model.profile.get('llm_model').get('name')))
        config.setdefault("callbacks", callbacks)
        return config

    def invoke_chain(self, chain: RunnableSerializable[Any, str], agent_input: dict, input_object: InputObject,
                     **kwargs):
        if not input_object.get_data('output_stream'):
            res = chain.invoke(input=agent_input, config=self.get_run_config())
            return res
        result = []
        for token in chain.stream(input=agent_input, config=self.get_run_config()):
            self.add_output_stream(input_object.get_data('output_stream', None), token)
            result.append(token)
        self.add_output_stream(input_object.get_data('output_stream', None), '\n\n')
        return self.generate_result(result)
