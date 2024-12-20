# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/17 14:26
# @Author  : weizjajj
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: rag_agent_case_template.py

import datetime
from threading import Thread

from langchain_core.output_parsers import StrOutputParser
from langchain_core.utils.json import parse_json_markdown

from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.memory.memory import Memory
from agentuniverse.agent.memory.message import Message
from agentuniverse.agent.template.agent_template import AgentTemplate
from agentuniverse.agent.template.rag_agent_template import RagAgentTemplate
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager
from agentuniverse.base.util.agent_util import assemble_memory_input, assemble_memory_output
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.prompt import Prompt


class RagAgentCaseTemplate(RagAgentTemplate):

    def summarize_memory(self, agent_input: dict, memory: Memory):
        session_id = agent_input.get('session_id')
        if not session_id:
            session_id = FrameworkContextManager().get_context('session_id')
            agent_input['session_id'] = session_id

        def do_summarize():
            summarized_memory = memory.summarize_memory(
                **self.get_memory_params(agent_input)
            )
            message = Message(content=summarized_memory, source=self.agent_model.info.get('name'), type='summarize',
                              metadata={
                                  'timestamp': datetime.datetime.now(),
                                  'gmt_created': datetime.datetime.now().timestamp(),
                                  "session_id": session_id
                              })
            memory.add([message], session_id=session_id)

        Thread(target=do_summarize).start()

    def load_summarize_memory(self, memory: Memory, session_id) -> str:
        if session_id is None:
            session_id = FrameworkContextManager().get_context('session_id')
        result = memory.get(
            session_id=session_id,
            agent_id=self.agent_model.info.get('name'),
            memory_type='summarize'
        )
        if len(result) == 0:
            return "no summarize memory"
        return result[-1].content

    def execute_query(self, input: str):
        agent_instance: AgentTemplate = AgentManager().get_instance_obj('question_agent_case')
        output_object = agent_instance.run(input=input)
        output = output_object.get_data('output')
        query_info = parse_json_markdown(output)
        if not query_info.get('need_google_search'):
            return "no_question"

        questions = query_info.get('search_questions')
        tool = ToolManager().get_instance_obj('google_search_tool')

        background = []
        for question in questions:
            background.append(tool.run(input=question))

        return "\n\n".join(background)

    def customized_execute(self, input_object: InputObject, agent_input: dict, memory: Memory, llm: LLM, prompt: Prompt,
                           **kwargs) -> dict:
        knowledge_res: str = self.execute_query(agent_input.get('input'))
        agent_input['background'] = knowledge_res
        assemble_memory_input(memory, agent_input, self.get_memory_params(agent_input))
        if not agent_input['chat_history']:
            agent_input['chat_history'] = "No Chat History"
        summarize_memory = self.load_summarize_memory(memory, agent_input.get('session_id'))
        agent_input['background'] = (agent_input['background']
                                     + f"\nsummarize_memory:\n {summarize_memory}")
        process_llm_token(llm, prompt.as_langchain(), self.agent_model.profile, agent_input)
        chain = prompt.as_langchain() | llm.as_langchain_runnable(
            self.agent_model.llm_params()) | StrOutputParser()
        res = self.invoke_chain(chain, agent_input, input_object, **kwargs)
        self.add_output_stream(input_object.get_data('output_stream'), res)
        self.summarize_memory(agent_input, memory)
        return {**agent_input, 'output': res}
