# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/10/18 15:25
# @Author  : weizjajj
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: opinion_inject_agent.py

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject


class OpinionInjectAgent(Agent):
    """
    An agent that injects opinions into the input.
    """

    def input_keys(self) -> list[str]:
        return ['data_fining_result']

    def output_keys(self) -> list[str]:
        return ['matched_opinions']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        for key in input_object.to_dict():
            agent_input[key] = input_object.get_data(key)
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        matched_opinions = [
            {
                "opinion": opinion["opinion"],
                "type": opinion["type"],
            } for opinion in planner_result.get('matched_opinions')
        ]
        return {"matched_opinions": matched_opinions}
