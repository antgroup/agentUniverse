# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/9/29 15:51
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: agent_template.py
from abc import ABC
from typing import Optional, Any, List
from queue import Queue

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable

from agentuniverse.agent.action.knowledge.knowledge import Knowledge
from agentuniverse.agent.action.knowledge.knowledge_manager import KnowledgeManager
from agentuniverse.agent.action.knowledge.store.document import Document
from agentuniverse.agent.action.tool.tool import Tool
from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.agent.memory.memory_manager import MemoryManager
from agentuniverse.agent.memory.message import Message
from agentuniverse.base.config.component_configer.configers.agent_configer import AgentConfiger
from agentuniverse.base.util.agent_util import assemble_memory_input, assemble_memory_output
from agentuniverse.base.util.common_util import stream_output
from agentuniverse.base.util.memory_util import generate_messages
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.llm.llm_manager import LLMManager
from agentuniverse.prompt.chat_prompt import ChatPrompt
from agentuniverse.prompt.prompt import Prompt
from agentuniverse.prompt.prompt_manager import PromptManager
from agentuniverse.prompt.prompt_model import AgentPromptModel


class AgentTemplate(Agent, ABC):
    llm_name: Optional[str] = ''
    memory_name: Optional[str] = None
    tool_names: Optional[list[str]] = None
    knowledge_names: Optional[list[str]] = None
    prompt_version: Optional[str] = None

    def execute(self, input_object: InputObject, agent_input: dict, **kwargs) -> dict:
        memory: Memory = self.process_memory(agent_input, **kwargs)
        llm: LLM = self.process_llm(**kwargs)
        prompt: Prompt = self.process_prompt(agent_input, **kwargs)
        return self.customized_execute(input_object, agent_input, memory, llm, prompt, **kwargs)

    async def async_execute(self, input_object: InputObject, agent_input: dict, **kwargs) -> dict:
        memory: Memory = self.process_memory(agent_input, **kwargs)
        llm: LLM = self.process_llm(**kwargs)
        prompt: Prompt = self.process_prompt(agent_input, **kwargs)
        return await self.customized_async_execute(input_object, agent_input, memory, llm, prompt, **kwargs)

    def customized_execute(self, input_object: InputObject, agent_input: dict, memory: Memory, llm: LLM, prompt: Prompt,
                           **kwargs) -> dict:
        assemble_memory_input(memory, agent_input)
        process_llm_token(llm, prompt.as_langchain(), self.agent_model.profile, agent_input)
        chain = prompt.as_langchain() | llm.as_langchain_runnable(
            self.agent_model.llm_params()) | StrOutputParser()
        res = self.invoke_chain(chain, agent_input, input_object, **kwargs)
        assemble_memory_output(memory=memory,
                               agent_input=agent_input,
                               content=f"Human: {agent_input.get('input')}, AI: {res}")
        self.add_output_stream(input_object.get_data('output_stream'), res)
        return {**agent_input, 'output': res}

    async def customized_async_execute(self, input_object: InputObject, agent_input: dict, memory: Memory,
                                       llm: LLM, prompt: Prompt, **kwargs) -> dict:
        assemble_memory_input(memory, agent_input)
        process_llm_token(llm, prompt.as_langchain(), self.agent_model.profile, agent_input)
        chain = prompt.as_langchain() | llm.as_langchain_runnable(
            self.agent_model.llm_params()) | StrOutputParser()
        res = await self.async_invoke_chain(chain, agent_input, input_object, **kwargs)
        assemble_memory_output(memory=memory,
                               agent_input=agent_input,
                               content=f"Human: {agent_input.get('input')}, AI: {res}")
        self.add_output_stream(input_object.get_data('output_stream'), res)
        return {**agent_input, 'output': res}

    def process_llm(self, **kwargs) -> LLM:
        return LLMManager().get_instance_obj(self.llm_name)

    def process_memory(self, agent_input: dict, **kwargs) -> Memory | None:
        memory: Memory = MemoryManager().get_instance_obj(component_instance_name=self.memory_name)
        if memory is None:
            return None

        chat_history: list = agent_input.get('chat_history')
        # generate a list of temporary messages from the given chat history and add them to the memory instance.
        temporary_messages: list[Message] = generate_messages(chat_history)
        if temporary_messages:
            memory.add(temporary_messages, **agent_input)

        params: dict = dict()
        params['agent_llm_name'] = self.llm_name
        return memory.set_by_agent_model(**params)

    def process_prompt(self, agent_input: dict, **kwargs) -> ChatPrompt:
        expert_framework = agent_input.pop('expert_framework', '') or ''

        profile: dict = self.agent_model.profile

        profile_instruction = profile.get('instruction')
        profile_instruction = expert_framework + profile_instruction if profile_instruction else profile_instruction

        profile_prompt_model: AgentPromptModel = AgentPromptModel(introduction=profile.get('introduction'),
                                                                  target=profile.get('target'),
                                                                  instruction=profile_instruction)

        # get the prompt by the prompt version
        version_prompt: Prompt = PromptManager().get_instance_obj(self.prompt_version)

        if version_prompt is None and not profile_prompt_model:
            raise Exception("Either the `prompt_version` or `introduction & target & instruction`"
                            " in agent profile configuration should be provided.")
        if version_prompt:
            version_prompt_model: AgentPromptModel = AgentPromptModel(
                introduction=getattr(version_prompt, 'introduction', ''),
                target=getattr(version_prompt, 'target', ''),
                instruction=expert_framework + getattr(version_prompt, 'instruction', ''))
            profile_prompt_model = profile_prompt_model + version_prompt_model

        chat_prompt = ChatPrompt().build_prompt(profile_prompt_model, ['introduction', 'target', 'instruction'])
        image_urls: list = agent_input.pop('image_urls', []) or []
        if image_urls:
            chat_prompt.generate_image_prompt(image_urls)
        return chat_prompt

    def invoke_chain(self, chain: RunnableSerializable[Any, str], agent_input: dict, input_object: InputObject,
                     **kwargs):
        if not input_object.get_data('output_stream'):
            res = chain.invoke(input=agent_input)
            return res
        result = []
        for token in chain.stream(input=agent_input):
            stream_output(input_object.get_data('output_stream', None), {
                'type': 'token',
                'data': {
                    'chunk': token,
                    'agent_info': self.agent_model.info
                }
            })
            result.append(token)
        return "".join(result)

    async def async_invoke_chain(self, chain: RunnableSerializable[Any, str], agent_input: dict,
                                 input_object: InputObject, **kwargs):
        if not input_object.get_data('output_stream'):
            res = await chain.ainvoke(input=agent_input)
            return res
        result = []
        async for token in chain.astream(input=agent_input):
            stream_output(input_object.get_data('output_stream', None), {
                'type': 'token',
                'data': {
                    'chunk': token,
                    'agent_info': self.agent_model.info
                }
            })
            result.append(token)
        return "".join(result)

    def invoke_tools(self, input_object: InputObject, **kwargs):
        if not self.tool_names:
            return ''

        tool_results: list = list()

        for tool_name in self.tool_names:
            tool: Tool = ToolManager().get_instance_obj(tool_name)
            if tool is None:
                continue
            tool_input = {key: input_object.get_data(key) for key in tool.input_keys}
            tool_results.append(str(tool.run(**tool_input)))
        return "\n\n".join(tool_results)

    def invoke_knowledge(self, query_str: str, input_object: InputObject, **kwargs):
        if not self.knowledge_names or not query_str:
            return ''

        knowledge_results: list = list()

        for knowledge_name in self.knowledge_names:
            knowledge: Knowledge = KnowledgeManager().get_instance_obj(knowledge_name)
            if knowledge is None:
                continue
            knowledge_res: List[Document] = knowledge.query_knowledge(
                query_str=query_str,
                **input_object.to_dict()
            )
            knowledge_results.append(knowledge.to_llm(knowledge_res))
        return "\n\n".join(knowledge_results)

    def validate_required_params(self):
        pass

    def add_output_stream(self, output_stream: Queue, agent_output: str) -> None:
        pass

    def initialize_by_component_configer(self, component_configer: AgentConfiger) -> 'AgentTemplate':
        super().initialize_by_component_configer(component_configer)
        self.llm_name = self.agent_model.profile.get('llm_model', {}).get('name')
        self.memory_name = self.agent_model.memory.get('name')
        self.tool_names = self.agent_model.action.get('tool', [])
        self.knowledge_names = self.agent_model.action.get('knowledge', [])
        return self
