# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from agentuniverse.agent.security.default.tool.default_mask_tool import DefaultMaskTool
# @Time    : 2024/4/8 20:58
# @Author  : jerry.zzw 
# @Email   : jerry.zzw@antgroup.com
# @FileName: server_application.py
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse
from examples.sample_standard_app.intelligence.agentic.tool.mock_search_tool import MockSearchTool


class ServerApplication:
    """
    Server application.
    """

    @classmethod
    def start(cls):
        AgentUniverse().start()
        start_web_server()


if __name__ == "__main__":
    AgentUniverse().start()
    mask_tool = MockSearchTool()
    res = mask_tool.run(input='测试')
    print(res)
