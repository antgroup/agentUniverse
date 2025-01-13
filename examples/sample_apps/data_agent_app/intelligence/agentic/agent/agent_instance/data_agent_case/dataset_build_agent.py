# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/7/5 15:07
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: dataset_build_agent.py
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from typing import Tuple, List, Any, Optional

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.util.logging.logging_util import LOGGER
from examples.sample_apps.data_agent_app.intelligence.utils.common.jsonl_file_util import JsonFileWriter, JsonFileReader


class DatasetBuildAgent(Agent):
    """Dataset Build Agent class."""

    executor: Optional[Any] = ThreadPoolExecutor(max_workers=1, thread_name_prefix="data_agent")

    def input_keys(self) -> list[str]:
        """Return the input keys of the Agent."""
        return ['queryset_path']

    def output_keys(self) -> list[str]:
        """Return the output keys of the Agent."""
        return ['query_answer_list']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        """Agent parameter parsing.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input preparsed by the agent.
        Returns:
            dict: agent input parsed from `input_object` by the user.
        """
        agent_input['queryset_path'] = input_object.get_data('queryset_path')
        agent_input['turn'] = input_object.get_data('turn', 1)
        agent_input['candidate'] = input_object.get_data('candidate')
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        """Planner result parser.

        Args:
            planner_result(dict): Planner result
        Returns:
            dict: Agent result object.
        """
        return planner_result

    def execute(self, input_object: InputObject, agent_input: dict):
        """Execute agent instance.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input parsed from `input_object` by the user.
        """
        # init thread pool
        profile = self.agent_model.profile or {}
        self.executor = ThreadPoolExecutor(
            max_workers=profile.get('concurrency_level') if profile.get('concurrency_level') else 1,
            thread_name_prefix="data_agent")

        # step1: build q&a dataset from the candidate agent which needs to be evaluated.
        query_answer_list = self.build_dataset(agent_input)
        input_object.add_data('query_answer_list', query_answer_list)

        LOGGER.info("-------------------------------------------")
        LOGGER.info("End: build q&a dataset from the candidate agent done.")
        LOGGER.info("-------------------------------------------")

        # step2: write the q&a dataset to json file.
        date = input_object.get_data('date', '')
        for i in range(len(query_answer_list)):
            one_turn_query_answer_list = query_answer_list[i]
            json_writer = JsonFileWriter(f'dataset_turn_{i + 1}_{date}')
            json_writer.write_json_query_answer_list(one_turn_query_answer_list)
        LOGGER.info(f"Progress: write the q&a dataset to local jsonl files.")
        return {'query_answer_list': query_answer_list}

    def build_dataset(self, agent_input: dict) -> List[List[Tuple[str, str]]]:
        """Build q&a dataset from the candidate agent which needs to be evaluated."""

        candidate_agent_name = agent_input.get('candidate') \
            if agent_input.get('candidate') else self.agent_model.profile.get('candidate', '')
        # get the candidate agent which needs to be evaluated
        candidate_agent: Agent = AgentManager().get_instance_obj(candidate_agent_name)
        if not candidate_agent:
            raise ValueError('The agent instance corresponding to `candidate` parameter is empty')

        # init jsonl file reader
        jsonl_file_reader = JsonFileReader(agent_input.get('queryset_path'))
        # read query list
        query_list = jsonl_file_reader.read_json_obj_list()
        if not query_list:
            raise ValueError('query list information read from queryset_path is empty')

        # init the input and output key in agent
        first_input_key = candidate_agent.input_keys()[0]
        first_output_key = candidate_agent.output_keys()[0]

        query_answer_list = []

        for i in range(agent_input.get('turn')):
            LOGGER.info("-------------------------------------------")
            LOGGER.info(f"Start: build q&a dataset from the candidate agent `{candidate_agent_name}`, turn {i + 1}.")
            one_turn_query_answer_list = []
            futures_to_query = {}

            # single turn query and answer processing.
            for j in range(len(query_list)):
                query_dict: dict = query_list[j]
                if query_dict:
                    # run the target agent
                    future = self.executor.submit(candidate_agent.run, **query_dict)
                    futures_to_query[future] = query_dict

            done, not_done = wait(futures_to_query.keys(), return_when=ALL_COMPLETED)

            for future in done:
                output_object: OutputObject = future.result()
                # note: the first index of input_keys and output_keys is identified as the prompt and answer.
                query = futures_to_query.get(future, {}).get(first_input_key, '')
                answer = output_object.get_data(first_output_key, '')

                one_turn_query_answer_list.append((query, answer))
                LOGGER.info(f"Progress: the turn {i + 1} query: `{query}` has generated the answer successfully.")

            LOGGER.info(f"End: the turn {i + 1} has generated the answer successfully.")

            # build q&a dataset
            query_answer_list.append(one_turn_query_answer_list)
        return query_answer_list
