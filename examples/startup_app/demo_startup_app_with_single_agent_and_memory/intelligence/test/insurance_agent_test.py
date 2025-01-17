# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/26 17:18
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: pet_insurance_agent_test.py
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
import uuid

from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

AgentUniverse().start(config_path='../../config/config.toml', core_mode=True)


def chat(question: str, session_id: str):
    instance: Agent = AgentManager().get_instance_obj('insurance_agent')
    output_object: OutputObject = instance.run(input=question, session_id=session_id)
    print(output_object.get_data('output') + '\n')


if __name__ == '__main__':
    s_id = str(uuid.uuid4())
    FrameworkContextManager().set_context('session_id', s_id)
    FrameworkContextManager().set_context('trace_id', str(uuid.uuid4()))
    chat("保险产品A怎么续保", s_id)
    FrameworkContextManager().set_context('trace_id', uuid.uuid4().hex)
    chat("我刚才问了什么问题", s_id)
