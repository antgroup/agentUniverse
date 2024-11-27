# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/6/4 21:27
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_react_agent.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class ReActAgentTest(unittest.TestCase):

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_react_agent(self):
        """Test demo reAct agent."""
        instance: Agent = AgentManager().get_instance_obj('demo_nl2api_agent')
        output_object: OutputObject = instance.run(input='1+3/2+10-4*3等于多少')
        print(output_object.to_dict())


if __name__ == '__main__':
    unittest.main()
