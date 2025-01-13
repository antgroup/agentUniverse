# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/3/12 19:36
# @Author  : heji
# @Email   : lc299034@antgroup.com
# @FileName: agent.py
import json
from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional, Any, List

from langchain_core.runnables import RunnableSerializable
from langchain_core.utils.json import parse_json_markdown

from agentuniverse.agent.action.knowledge.knowledge import Knowledge
from agentuniverse.agent.action.knowledge.knowledge_manager import KnowledgeManager
from agentuniverse.agent.action.knowledge.store.document import Document
from agentuniverse.agent.action.tool.tool import Tool
from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.agent.agent_model import AgentModel
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.agent.memory.memory_manager import MemoryManager
from agentuniverse.agent.memory.message import Message
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.agent.plan.planner.planner_manager import PlannerManager
from agentuniverse.agent.security.security_manager import SecurityManager
from agentuniverse.base.annotation.trace import trace_agent
from agentuniverse.base.component.component_base import ComponentBase
from agentuniverse.base.component.component_enum import ComponentEnum
from agentuniverse.base.config.application_configer.application_config_manager \
    import ApplicationConfigManager
from agentuniverse.base.config.component_configer.configers.agent_configer \
    import AgentConfiger
from agentuniverse.base.util.common_util import stream_output
from agentuniverse.base.util.logging.logging_util import LOGGER
from agentuniverse.base.util.memory_util import generate_messages
from agentuniverse.llm.llm import LLM
from agentuniverse.llm.llm_manager import LLMManager
from agentuniverse.prompt.chat_prompt import ChatPrompt
from agentuniverse.prompt.prompt import Prompt
from agentuniverse.prompt.prompt_manager import PromptManager
from agentuniverse.prompt.prompt_model import AgentPromptModel


class Agent(ComponentBase, ABC):
    """The parent class of all agent models, containing only attributes."""

    agent_model: Optional[AgentModel] = None

    def __init__(self):
        """Initialize the AgentModel with the given keyword arguments."""
        super().__init__(component_type=ComponentEnum.AGENT)

    @abstractmethod
    def input_keys(self) -> list[str]:
        """Return the input keys of the Agent."""
        pass

    @abstractmethod
    def output_keys(self) -> list[str]:
        """Return the output keys of the Agent."""
        pass

    @abstractmethod
    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        """Agent parameter parsing.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input preparsed by the agent.
        Returns:
            dict: agent input parsed from `input_object` by the user.
        """
        pass

    @abstractmethod
    def parse_result(self, agent_result: dict) -> dict:
        """Agent result parser.

        Args:
            agent_result(dict): The raw result of the agent.
        Returns:
            dict: The parsed result of the agent
        """
        pass

    @trace_agent
    def run(self, **kwargs) -> OutputObject:
        """Agent instance running entry.

        Returns:
            OutputObject: Agent execution result
        """
        self.input_check(kwargs)
        input_object = InputObject(kwargs)
        security_base = SecurityManager().get_instance_obj(self.agent_model.security)
        security_base.pre_invoke(input_object)

        agent_input = self.pre_parse_input(input_object)
        input_object.add_data('security', security_base)

        planner_result = self.execute(input_object, agent_input)

        agent_result = self.parse_result(planner_result)

        self.output_check(agent_result)
        output_object = OutputObject(agent_result)
        security_base.final_invoke(output_object)
        return output_object

    @trace_agent
    async def async_run(self, **kwargs) -> OutputObject:
        self.input_check(kwargs)
        input_object = InputObject(kwargs)

        agent_input = self.pre_parse_input(input_object)

        agent_result = await self.async_execute(input_object, agent_input)

        agent_result = self.parse_result(agent_result)

        self.output_check(agent_result)
        output_object = OutputObject(agent_result)
        return output_object

    def execute(self, input_object: InputObject, agent_input: dict) -> dict:
        """Execute agent instance.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input parsed from `input_object` by the user.

        Returns:
            dict: planner result generated by the planner execution.
        """
        planner_base: Planner = PlannerManager().get_instance_obj(self.agent_model.plan.get('planner').get('name'))
        planner_result = planner_base.invoke(self.agent_model, agent_input, input_object)
        return planner_result

    async def async_execute(self, input_object: InputObject, agent_input: dict) -> dict:
        pass

    def pre_parse_input(self, input_object) -> dict:
        """Agent execution parameter pre-parsing.

        Args:
            input_object (InputObject): input parameters passed by the user.
        Returns:
            dict: agent input preparsed by the agent.
        """
        agent_input = dict()
        agent_input['chat_history'] = input_object.get_data('chat_history') or ''
        agent_input['background'] = input_object.get_data('background') or ''
        agent_input['image_urls'] = input_object.get_data('image_urls') or []
        agent_input['date'] = datetime.now().strftime('%Y-%m-%d')
        agent_input['session_id'] = input_object.get_data('session_id') or ''
        agent_input['agent_id'] = self.agent_model.info.get('name', '')
        self.parse_input(input_object, agent_input)
        return agent_input

    def get_instance_code(self) -> str:
        """Return the full name of the agent."""
        appname = ApplicationConfigManager().app_configer.base_info_appname
        name = self.agent_model.info.get('name')
        return (f'{appname}.'
                f'{self.component_type.value.lower()}.{name}')

    def input_check(self, kwargs: dict):
        """Agent parameter check."""
        for key in self.input_keys():
            if key not in kwargs.keys():
                raise Exception(f'Input must have key: {key}.')

    def output_check(self, kwargs: dict):
        """Agent result check."""
        if not isinstance(kwargs, dict):
            raise Exception('Output type must be dict.')
        for key in self.output_keys():
            if key not in kwargs.keys():
                raise Exception(f'Output must have key: {key}.')

    def initialize_by_component_configer(self, component_configer: AgentConfiger) -> 'Agent':
        """Initialize the Agent by the AgentConfiger object.

        Args:
            component_configer(AgentConfiger): the ComponentConfiger object
        Returns:
            Agent: the Agent object
        """
        agent_config: Optional[AgentConfiger] = component_configer.load()
        info: Optional[dict] = agent_config.info
        profile: Optional[dict] = agent_config.profile
        plan: Optional[dict] = agent_config.plan
        memory: Optional[dict] = agent_config.memory
        action: Optional[dict] = agent_config.action
        security: Optional[str] = agent_config.security
        agent_model: Optional[AgentModel] = AgentModel(info=info, profile=profile,
                                                       plan=plan, memory=memory, action=action, security=security)
        self.agent_model = agent_model
        return self

    def langchain_run(self, input: str, callbacks=None, **kwargs):
        """Run the agent model using LangChain."""
        try:
            parse_result = parse_json_markdown(input)
        except Exception as e:
            LOGGER.error(f"langchain run parse_json_markdown error,input(parse_result) error({str(e)})")
            return "Error , Your Action Input is not a valid JSON string"
        output_object = self.run(**parse_result, callbacks=callbacks, **kwargs)
        result_dict = {}
        for key in self.output_keys():
            result_dict[key] = output_object.get_data(key)
        return result_dict

    def as_langchain_tool(self):
        """Convert to LangChain tool."""
        from langchain.agents.tools import Tool
        format_dict = {}
        for key in self.input_keys():
            format_dict.setdefault(key, "input val")
        format_str = json.dumps(format_dict)

        args_description = f"""
        to use this tool,your input must be a json string,must contain all keys of {self.input_keys()},
        and the value of the key must be a json string,the format of the json string is as follows:
        ```{format_str}```
        """
        return Tool(
            name=self.agent_model.info.get("name"),
            func=self.langchain_run,
            description=self.agent_model.info.get("description") + args_description
        )

    def process_llm(self, **kwargs) -> LLM:
        llm_name = kwargs.get('llm_name') or self.agent_model.profile.get('llm_model', {}).get('name')
        return LLMManager().get_instance_obj(llm_name)

    def process_memory(self, agent_input: dict, **kwargs) -> Memory | None:
        memory_name = kwargs.get('memory_name') or self.agent_model.memory.get('name')
        memory: Memory = MemoryManager().get_instance_obj(memory_name)
        if memory is None:
            return None

        chat_history: list = agent_input.get('chat_history')
        # generate a list of temporary messages from the given chat history and add them to the memory instance.
        temporary_messages: list[Message] = generate_messages(chat_history)
        if temporary_messages:
            memory.add(temporary_messages, **agent_input)

        params: dict = dict()
        params['agent_llm_name'] = kwargs.get('llm_name') or self.agent_model.profile.get('llm_model', {}).get('name')
        return memory.set_by_agent_model(**params)

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

    def invoke_tools(self, input_object: InputObject, **kwargs) -> str:
        tool_names = kwargs.get('tool_names') or self.agent_model.action.get('tool', [])
        if not tool_names:
            return ''

        tool_results: list = list()

        for tool_name in tool_names:
            tool: Tool = ToolManager().get_instance_obj(tool_name)
            if tool is None:
                continue
            tool_input = {key: input_object.get_data(key) for key in tool.input_keys}
            tool_results.append(str(tool.run(**tool_input)))
        return "\n\n".join(tool_results)

    def invoke_knowledge(self, query_str: str, input_object: InputObject, **kwargs) -> str:
        knowledge_names = kwargs.get('knowledge_names') or self.agent_model.action.get('knowledge', [])
        if not knowledge_names or not query_str:
            return ''

        knowledge_results: list = list()

        for knowledge_name in knowledge_names:
            knowledge: Knowledge = KnowledgeManager().get_instance_obj(knowledge_name)
            if knowledge is None:
                continue
            knowledge_res: List[Document] = knowledge.query_knowledge(
                query_str=query_str,
                **input_object.to_dict()
            )
            knowledge_results.append(knowledge.to_llm(knowledge_res))
        return "\n\n".join(knowledge_results)

    def process_prompt(self, agent_input: dict, **kwargs) -> ChatPrompt:
        expert_framework = agent_input.pop('expert_framework', '') or ''

        profile: dict = self.agent_model.profile

        profile_instruction = profile.get('instruction')
        profile_instruction = expert_framework + profile_instruction if profile_instruction else profile_instruction

        profile_prompt_model: AgentPromptModel = AgentPromptModel(introduction=profile.get('introduction'),
                                                                  target=profile.get('target'),
                                                                  instruction=profile_instruction)

        # get the prompt by the prompt version
        prompt_version = kwargs.get('prompt_version') or self.agent_model.profile.get('prompt_version')
        version_prompt: Prompt = PromptManager().get_instance_obj(prompt_version)

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
