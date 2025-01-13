# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/7/1 16:48
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_data_agent.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.base.agentuniverse import AgentUniverse


class DataAgentTest(unittest.TestCase):
    """Test cases for the data agent"""

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_data_agent(self):
        instance: Agent = AgentManager().get_instance_obj('data_agent')
        instance.run(queryset_path='', turn=2)


if __name__ == '__main__':
    unittest.main()
