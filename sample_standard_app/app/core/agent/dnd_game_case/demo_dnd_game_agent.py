# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/15 12:42
# @Author  : xutingdong
# @Email   : xutingdong.xtd@antgroup.com
# @FileName: demo_dnd_game_agent.py
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject


class DndGameAgent(Agent):
    def input_keys(self) -> list[str]:
        return ['input']

    def output_keys(self) -> list[str]:
        return ['output']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        agent_input['input'] = input_object.get_data('input')
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        return planner_result
