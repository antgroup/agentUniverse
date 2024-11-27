# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/4/15 11:01
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_planning_agent.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class PlanningAgentTest(unittest.TestCase):
    """Test cases for the planning agent"""

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_planning_agent(self):
        """Test demo planning agent."""

        instance: Agent = AgentManager().get_instance_obj('demo_planning_agent')
        output_object: OutputObject = instance.run(input='分析下巴菲特减持比亚迪的原因')
        res_info = f"\nPlanning agent execution result is :\n"
        for index, one_framework in enumerate(output_object.get_data('framework')):
            res_info += f"[{index + 1}] {one_framework} \n"
        print(res_info)


if __name__ == '__main__':
    unittest.main()
