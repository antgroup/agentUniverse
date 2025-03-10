from queue import Queue
from typing import Any

from langchain_core.runnables import RunnableSerializable

from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.template.executing_agent_template import ExecutingAgentTemplate
from agentuniverse.agent.template.openai_protocol_template import OpenAIProtocolTemplate
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.prompt import Prompt


class ExecutingOpenAIAgentTemplate(OpenAIProtocolTemplate, ExecutingAgentTemplate):
    def parse_openai_protocol_output(self, output_object: OutputObject) -> OutputObject:
        return output_object

    def customized_execute(self, input_object: InputObject, agent_input: dict, memory: Memory, llm: LLM, prompt: Prompt,
                           **kwargs) -> dict:
        return ExecutingAgentTemplate.customized_execute(self, input_object, agent_input, memory, llm, prompt, **kwargs)

    def invoke_chain(self, chain: RunnableSerializable[Any, str], agent_input: dict, input_object: InputObject,
                     **kwargs):
        if not self.judge_chain_stream(chain):
            res = chain.invoke(input=agent_input, config=self.get_run_config())
            return res
        result = []
        for token in chain.stream(input=agent_input, config=self.get_run_config()):
            result.append(token)
        input = agent_input.get('input')
        self.add_output_stream(input_object.get_data('output_stream', None),
                               f'#### Question:{input} \n\n Answer: {self.generate_result(result)}\n\n')
        return self.generate_result(result)

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        self.add_output_stream(input_object.get_data('output_stream', None), '## Executing  \n\n')
        return super().parse_input(input_object, agent_input)
