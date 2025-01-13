# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/6/7 10:49
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_discussion_agents.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class DiscussionAgentsTest(unittest.TestCase):

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_discussion_agents(self):
        instance: Agent = AgentManager().get_instance_obj('discussion_group_agent')
        output_object: OutputObject = instance.run(input='甜粽子好吃还是咸粽子好吃')


if __name__ == '__main__':
    unittest.main()
