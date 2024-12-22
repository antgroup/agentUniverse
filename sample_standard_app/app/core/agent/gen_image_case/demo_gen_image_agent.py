# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/03 19:10
# @Author  : xutingdong
# @Email   : xutingdong.xtd@antgroup.com
# @FileName: demo_gen_image_agent.py

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.action.tool.tool_manager import ToolManager


class GenImageAgent(Agent):
    def input_keys(self) -> list[str]:
        return ['input']

    def output_keys(self) -> list[str]:
        return ['output']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        agent_input['input'] = input_object.get_data('input')
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        return {'output': ''}

    def execute(self, input_object: InputObject, agent_input: dict) -> dict:
        action: dict = self.agent_model.action or dict()
        tools: list = action.get('tool') or list()
        for tool_name in tools:
            tool = ToolManager().get_instance_obj(tool_name)
            if tool is None:
                continue
            tool.run(**input_object.to_dict())