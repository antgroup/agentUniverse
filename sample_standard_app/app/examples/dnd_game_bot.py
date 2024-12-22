# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/15 12:42
# @Author  : xutingdong
# @Email   : xutingdong.xtd@antgroup.com
# @FileName: dnd_game_bot.py

from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start(config_path='../../config/config.toml')


def chat(question: str):
    """ Rag agent example.

    The rag agent in agentUniverse becomes a chatbot and can ask questions to get the answer.
    """

    instance: Agent = AgentManager().get_instance_obj('demo_dnd_game_agent')
    instance.run(input=question)


if __name__ == '__main__':
    chat("游戏开始")
