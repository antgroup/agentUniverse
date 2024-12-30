# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/26 20:56
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: pet_insurance_expressing_agent.py
from langchain_core.output_parsers import StrOutputParser

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.base.util.logging.logging_util import LOGGER
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.prompt import Prompt


class PetInsuranceExpressingAgent(Agent):

    def input_keys(self) -> list[str]:
        return ['input', 'prod_description', 'search_context']

    def output_keys(self) -> list[str]:
        return ['output']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        agent_input['input'] = input_object.get_data('input')
        agent_input['prod_description'] = input_object.get_data('prod_description')
        agent_input['search_context'] = input_object.get_data('search_context')
        return agent_input

    def parse_result(self, agent_result: dict) -> dict:
        output = agent_result['output']
        LOGGER.info(f'智能体 pet_insurance_expressing_agent 执行结果为： {output}')
        return {**agent_result, 'output': output}

    def execute(self, input_object: InputObject, agent_input: dict, **kwargs) -> dict:
        # 1. get the llm instance.
        llm: LLM = self.process_llm(**kwargs)
        # 2. get the agent prompt.
        prompt: Prompt = self.process_prompt(agent_input, **kwargs)
        process_llm_token(llm, prompt.as_langchain(), self.agent_model.profile, agent_input)
        # 3. invoke agent.
        chain = prompt.as_langchain() | llm.as_langchain_runnable(
            self.agent_model.llm_params()) | StrOutputParser()
        res = self.invoke_chain(chain, agent_input, input_object, **kwargs)
        # 4. return result.
        return {**agent_input, 'output': res}
