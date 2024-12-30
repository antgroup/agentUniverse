# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/5/8 11:41
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: peer_chat_bot.py
from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

AgentUniverse().start(config_path='../../config/config.toml', core_mode=True)


def chat(question: str):
    """ Peer agents example.

    The peer agents in agentUniverse become a chatbot and can ask questions to get the answer.
    """
    FrameworkContextManager().set_context("session_id","test_weizj_005")
    # FrameworkContextManager().set_context("trace_id","005")
    instance: Agent = AgentManager().get_instance_obj('peer_agent_case')
    instance.run(input=question)


if __name__ == '__main__':
    chat("A股大涨的原因")
