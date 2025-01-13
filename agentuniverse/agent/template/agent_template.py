# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/9/29 15:51
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: agent_template.py
from abc import ABC
from typing import Optional
from queue import Queue

from langchain_core.output_parsers import StrOutputParser

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.base.config.component_configer.configers.agent_configer import AgentConfiger
from agentuniverse.base.util.agent_util import assemble_memory_input, assemble_memory_output
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.chat_prompt import ChatPrompt
from agentuniverse.prompt.prompt import Prompt


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

    def process_llm(self, **kwargs) -> LLM:
        return super().process_llm(llm_name=self.llm_name)

    def process_memory(self, agent_input: dict, **kwargs) -> Memory | None:
        return super().process_memory(agent_input=agent_input, memory_name=self.memory_name, llm_name=self.llm_name)

    def invoke_tools(self, input_object: InputObject, **kwargs) -> str:
        return super().invoke_tools(input_object=input_object, tool_names=self.tool_names)

    def invoke_knowledge(self, query_str: str, input_object: InputObject, **kwargs) -> str:
        return super().invoke_knowledge(query_str=query_str, input_object=input_object,
                                        knowledge_names=self.knowledge_names)

    def process_prompt(self, agent_input: dict, **kwargs) -> ChatPrompt:
        return super().process_prompt(agent_input=agent_input, prompt_version=self.prompt_version)
