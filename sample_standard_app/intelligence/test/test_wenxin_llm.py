# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/5/22 16:25
# @Author  : weizjajj 
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: test_wenxin_llm.py


import asyncio
import os
import time
import unittest

from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.llm.default.wenxin_llm import WenXinLLM
from agentuniverse.llm.llm_manager import LLMManager


class WenXinLLMTest(unittest.TestCase):
    """Test cases for the reviewing agent"""

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_reviewing_agent(self):
        llm: WenXinLLM = LLMManager().get_instance_obj("default_baichuan_llm")
        res = llm.call(
            messages=[{"role": "user", "content": "你好"}],
            streaming=True
        )
        print(res)
        for item in res:
            print(item)

        langchain_llm = llm.as_langchain()
        print(langchain_llm.invoke(input="你好"))
        time.sleep(1)
        asyncio.run(self.call_stream())

    async def call_stream(self):
        llm: WenXinLLM = LLMManager().get_instance_obj("default_qwen_llm")
        res = await llm.acall(
            messages=[{"role": "user", "content": "你好"}],
            streaming=True
        )
        print(res)
        async for item in res:
            print(item)

        langchain_llm = llm.as_langchain()
        res = await langchain_llm.ainvoke(input="你好")
        print(res)


if __name__ == '__main__':
    unittest.main()
