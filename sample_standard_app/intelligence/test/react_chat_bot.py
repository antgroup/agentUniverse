# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse

# @Time    : 2024/5/8 11:44
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: rag_chat_bot.py
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start(config_path='../../config/config.toml', core_mode=True)


def chat(question: str):
    """ Rag agent example.

    The rag agent in agentUniverse becomes a chatbot and can ask questions to get the answer.
    """

    instance: Agent = AgentManager().get_instance_obj('demo_react_agent')
    output_object: OutputObject = instance.run(input=question)
    res_info = f"\nReact chat bot execution result is :\n"
    res_info += output_object.get_data('output')
    print(res_info)


if __name__ == '__main__':
    # 获取python 命令直接执行时的 --question 参数
    parser = argparse.ArgumentParser(description="Chat bot for answering questions about birthdays.")
    parser.add_argument("--question", type=str, help="The question to ask.")
    args = parser.parse_args()
    if args.question:
        chat(args.question)
    else:
        chat("请给我一段可以计算三数之和的python代码")
