# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/3/25 14:58
# @Author  : heji
# @Email   : lc299034@antgroup.com
# @FileName: rag_planner.py
"""Rag planner module."""

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.agent_model import AgentModel
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.agent.memory.chat_memory import ChatMemory
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.base.util.memory_util import generate_memories
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.chat_prompt import ChatPrompt
from agentuniverse.prompt.prompt import Prompt
from agentuniverse.prompt.prompt_manager import PromptManager
from agentuniverse.prompt.prompt_model import AgentPromptModel
import re
import gradio as gr
from urllib import parse


class DndGamePlanner(Planner):
    """Rag planner class."""

    def invoke(self, agent_model: AgentModel, planner_input: dict,
               input_object: InputObject) -> dict:
        """Invoke the planner.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
            input_object (InputObject): The input parameters passed by the user.
        Returns:
            dict: The planner result.
        """
        planner_config = agent_model.plan.get('planner')
        # invoke agents
        return self.agents_run(agent_model, planner_input, input_object)

    def invoke_begin_agent(self, agent_model: AgentModel, planner_input: dict, input_object: InputObject) -> dict:
        """ Invoke the host agent.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
            input_object (InputObject): The input parameters passed by the user.
        Returns:
            dict: The planner result.
        """
        memory: ChatMemory = self.handle_memory(agent_model, planner_input)

        llm: LLM = self.handle_llm(agent_model)

        prompt: ChatPrompt = self.handle_prompt(agent_model, planner_input)
        process_llm_token(llm, prompt.as_langchain(), agent_model.profile, planner_input)

        chat_history = memory.as_langchain().chat_memory if memory else InMemoryChatMessageHistory()

        chain_with_history = RunnableWithMessageHistory(
            prompt.as_langchain() | llm.as_langchain(),
            lambda session_id: chat_history,
            history_messages_key="chat_history",
            input_messages_key=self.input_key,
        ) | StrOutputParser()
        res = self.invoke_chain(agent_model, chain_with_history, planner_input, chat_history, input_object)
        return {**planner_input, self.output_key: res, 'chat_history': generate_memories(chat_history)}

    def create_image(self, message):
        pattern = r"^(.*?)(:|：)(.*?)<(.*?)>"
        match = re.search(pattern, message, re.DOTALL)
        image = message
        if match:
            image = match.group(4).strip()
        print(image)
        input = parse.quote(image, safe='/')
        image_url = f'https://image.pollinations.ai/prompt/{input}'

        markdown_url = f"![image]({image_url})"
        return markdown_url
    def agents_run(self, agent_model: AgentModel, planner_input: dict, input_object: InputObject):
        """ Invoke the dnd game agent.

        Args:
            agent_model (AgentModel): Agent model object.
            agent_input (dict): Agent input object.
            input_object (InputObject): The input parameters passed by the user.
        Returns:
            dict: The planner result.
        """
        ref = self.invoke_begin_agent(agent_model, planner_input, input_object)
        chat_history = ref.get('chat_history', [])
        input_object.add_data('chat_history', chat_history)
        plot_agent = AgentManager().get_instance_obj('gen_plot_agent')

        def get_response(message):
            input_object.add_data('choice', message)

            output_object: OutputObject = plot_agent.run(**input_object.to_dict())
            current_output = output_object.get_data('output', '')

            chat_history.append({'content': message, 'type': 'human'})
            chat_history.append(
                {'content': f'{current_output}', 'type': 'ai'})
            input_object.add_data('chat_history', chat_history)

            return current_output

        def respond(message, history):
            bot_message = get_response(message)
            image = self.create_image(bot_message)
            history.append((message, bot_message + image))
            return "", history

        with gr.Blocks() as demo:
            chatbot = gr.Chatbot(placeholder=chat_history[1]['content'], height=2000)

            msg = gr.Textbox(label="Prompt")
            btn = gr.Button("Submit")
            clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

            btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
            msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

        gr.close_all()
        demo.launch()

    def handle_prompt(self, agent_model: AgentModel, planner_input: dict) -> ChatPrompt:
        """Prompt module processing.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
        Returns:
            ChatPrompt: The chat prompt instance.
        """
        profile: dict = agent_model.profile

        profile_prompt_model: AgentPromptModel = AgentPromptModel(introduction=profile.get('introduction'),
                                                                  target=profile.get('target'),
                                                                  instruction=profile.get('instruction'))

        # get the prompt by the prompt version
        prompt_version: str = profile.get('prompt_version')
        version_prompt: Prompt = PromptManager().get_instance_obj(prompt_version)

        if version_prompt is None and not profile_prompt_model:
            raise Exception("Either the `prompt_version` or `introduction & target & instruction`"
                            " in agent profile configuration should be provided.")
        if version_prompt:
            version_prompt_model: AgentPromptModel = AgentPromptModel(
                introduction=getattr(version_prompt, 'introduction', ''),
                target=getattr(version_prompt, 'target', ''),
                instruction=getattr(version_prompt, 'instruction', ''))
            profile_prompt_model = profile_prompt_model + version_prompt_model

        chat_prompt = ChatPrompt().build_prompt(profile_prompt_model, self.prompt_assemble_order)
        return chat_prompt
