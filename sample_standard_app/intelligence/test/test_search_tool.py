import os
import unittest

from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.base.agentuniverse import AgentUniverse


class SearchToolTest(unittest.TestCase):
    """
    Test cases for the rag agent
    """

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_rag_agent(self):
        """Test demo rag agent."""
        res = ToolManager().get_instance_obj("baidu_search_tool").run(input="今日黄金价格")
        print(res)


if __name__ == '__main__':
    unittest.main()
