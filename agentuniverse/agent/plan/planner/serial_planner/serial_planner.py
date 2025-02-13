# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/10/18 15:25
# @Author  : weizjajj
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: serial_planner.py

from agentuniverse.agent.action.tool.tool import Tool
from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.agent_model import AgentModel
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.base.util.logging.logging_util import LOGGER


def execute_tool_or_agent(name: str, manager_class, planner_input: dict,
                          runtime_params: dict):
    instance = manager_class.get_instance_obj(name)
    input_params = dict()
    input_params.update(runtime_params)

    if isinstance(instance, Tool):
        input_keys = instance.input_keys
    elif isinstance(instance, Agent):
        input_keys = instance.input_keys()
    else:
        raise ValueError(f"Unsupported instance type: {instance}")

    for key in input_keys:
        if key in input_params:
            continue
        if key not in planner_input:
            raise Exception(f"{key} is not in planner input")
        input_params[key] = planner_input.get(key)

    try:
        result = instance.run(**input_params)
        if isinstance(result, dict):
            planner_input.update(result)
        elif isinstance(result, OutputObject):
            planner_input.update(result.to_dict())
        else:
            planner_input[name] = result
        return result
    except Exception as e:
        raise Exception(f"Error executing {name}: {e}")


class SerialPlanner(Planner):
    """Executing planner class."""

    def invoke(self, agent_model: AgentModel, planner_input: dict, input_object: InputObject) -> dict:
        """Invoke the planner.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
            input_object (InputObject): The input parameters passed by the user.
        Returns:
            dict: The planner result.
        """
        output_stream = input_object.get_data('output_stream')
        if output_stream:
            planner_input.update({'output_stream': output_stream})
        return self.run_all_actions(agent_model, planner_input, input_object)

    def run_all_actions(self, agent_model: AgentModel, planner_input: dict, input_object: InputObject):
        if not isinstance(planner_input, dict):
            raise TypeError("planner_input must be a dictionary")

        serials: dict = agent_model.plan.get('planner')
        for key in serials:
            if key == 'name':
                continue
            tool = serials.get(key)
            tool_name = tool.get('name')
            runtime_params = tool.get('runtime_params') or dict()
            tool_type = tool.get('type') or 'tool'
            if tool_type == 'tool':
                LOGGER.info(f"start Executing tool: {tool_name}")
                res = execute_tool_or_agent(tool_name, ToolManager(), planner_input, runtime_params)
                self.stream_output(input_object, {
                    'data': res,
                    "type": "tool",
                    "agent_info": agent_model.info
                })
                LOGGER.info(f"finished execute tool {tool_name},execute result {res}")
            elif tool_type == 'agent':
                LOGGER.info(f"start Executing Agent: {tool_name}")
                res = execute_tool_or_agent(tool_name, AgentManager(), planner_input, runtime_params)
                self.stream_output(input_object, {
                    'data': res.to_dict(),
                    "type": "agent",
                    "agent_info": agent_model.info
                })
                LOGGER.info(f"finished execute agent {tool_name},execute result {res.to_dict()}")
            else:
                raise ValueError(f"Unsupported tool type: {tool_type}")
        return planner_input
