# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/5/20 16:24
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: monitor.py
import datetime
import json
import os
import uuid
from typing import Union, Optional

from pydantic import BaseModel

from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.annotation.singleton import singleton
from agentuniverse.base.config.configer import Configer
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

LLM_INVOCATION_SUBDIR = "llm_invocation"
AGENT_INVOCATION_SUBDIR = "agent_invocation"


@singleton
class Monitor(BaseModel):
    dir: Optional[str] = './monitor'
    activate: Optional[bool] = False

    def __init__(self, configer: Configer = None, **kwargs):
        super().__init__(**kwargs)
        if configer:
            config: dict = configer.value.get('MONITOR', {})
            self.dir = config.get('dir', './monitor')
            self.activate = config.get('activate', False)

    def trace_llm_invocation(self, source: str, llm_input: Union[str, dict], llm_output: Union[str, dict]) -> None:
        """Trace the llm invocation and save it to the monitor jsonl file."""
        if self.activate:
            try:
                import jsonlines
            except ImportError:
                raise ImportError(
                    "jsonlines is required to trace llm invocation: `pip install jsonlines`"
                )
            # get the current time
            date = datetime.datetime.now()
            llm_invocation = {
                "source": source,
                "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                "llm_input": llm_input,
                "llm_output": llm_output,
            }
            # files are stored in hours
            filename = f"llm_{date.strftime('%Y-%m-%d-%H')}.jsonl"
            # file path to save
            path_save = os.path.join(str(self._get_or_create_subdir(LLM_INVOCATION_SUBDIR)), filename)

            # write to jsonl
            with jsonlines.open(path_save, 'a') as writer:
                writer.write(llm_invocation)

    def trace_agent_invocation(self, source: str, agent_input: Union[str, dict],
                               agent_output: Union[str, dict]) -> None:
        """Trace the agent invocation and save it to the monitor jsonl file."""
        if self.activate:
            try:
                import jsonlines
            except ImportError:
                raise ImportError(
                    "jsonlines is required to trace llm invocation: `pip install jsonlines`"
                )
            # get the current time
            date = datetime.datetime.now()
            agent_invocation = {
                "source": source,
                "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                "agent_input": self.serialize_obj(agent_input),
                "agent_output": self.serialize_obj(agent_output),
            }
            # files are stored in hours
            filename = f"agent_{source}_{date.strftime('%Y-%m-%d-%H')}.jsonl"
            # file path to save
            path_save = os.path.join(str(self._get_or_create_subdir(AGENT_INVOCATION_SUBDIR)), filename)

            # write to jsonl
            with jsonlines.open(path_save, 'a') as writer:
                writer.write(agent_invocation)

    @staticmethod
    def init_trace_id():
        """Initialize the trace id in the framework context."""
        if FrameworkContextManager().get_context('trace_id') is None:
            FrameworkContextManager().set_context('trace_id', str(uuid.uuid4()))

    @staticmethod
    def init_invocation_chain():
        """Initialize the invocation chain in the framework context."""
        Monitor.init_trace_id()
        trace_id = FrameworkContextManager().get_context('trace_id')
        if FrameworkContextManager().get_context(trace_id + '_invocation_chain') is None:
            FrameworkContextManager().set_context(trace_id + '_invocation_chain', [])

    @staticmethod
    def pop_invocation_chain():
        """Pop the last chain node in invocation chain."""
        trace_id = FrameworkContextManager().get_context('trace_id')
        if trace_id is not None:
            invocation_chain: list = FrameworkContextManager().get_context(
                trace_id + '_invocation_chain')
            if invocation_chain is not None:
                invocation_chain.pop()
                FrameworkContextManager().set_context(
                    trace_id + '_invocation_chain', invocation_chain)

    @staticmethod
    def clear_invocation_chain():
        """Clear the invocation chain in the framework context."""
        trace_id = FrameworkContextManager().get_context('trace_id')
        if trace_id is not None:
            FrameworkContextManager().del_context(trace_id + '_invocation_chain')

    @staticmethod
    def add_invocation_chain(source: dict):
        """Add the source to the invocation chain"""
        trace_id = FrameworkContextManager().get_context('trace_id')
        if trace_id is not None:
            invocation_chain = FrameworkContextManager().get_context(trace_id + '_invocation_chain')
            if invocation_chain is not None:
                invocation_chain.append(source)
                FrameworkContextManager().set_context(trace_id + '_invocation_chain', invocation_chain)

    @staticmethod
    def get_trace_id():
        """Get the trace id in the framework context."""
        return FrameworkContextManager().get_context('trace_id')

    @staticmethod
    def get_invocation_chain():
        """Get the invocation chain in the framework context."""
        trace_id = FrameworkContextManager().get_context('trace_id')
        return FrameworkContextManager().get_context(trace_id + '_invocation_chain', []) if trace_id is not None else []

    @staticmethod
    def init_token_usage():
        """Initialize the token usage in the framework context."""
        Monitor.init_trace_id()
        trace_id = FrameworkContextManager().get_context('trace_id')
        if FrameworkContextManager().get_context(trace_id + '_token_usage') is None:
            FrameworkContextManager().set_context(trace_id + '_token_usage', {})

    @staticmethod
    def add_token_usage(cur_token_usage: dict):
        """Add the token usage to the framework context."""
        if cur_token_usage is None:
            return
        trace_id = FrameworkContextManager().get_context('trace_id')
        if trace_id is not None:
            old_token_usage: dict = FrameworkContextManager().get_context(trace_id + '_token_usage')
            if old_token_usage is not None:
                for key, value in cur_token_usage.items():
                    old_token_usage[key] = old_token_usage[key] + value if key in old_token_usage else value
                FrameworkContextManager().set_context(trace_id + '_token_usage', old_token_usage)

    @staticmethod
    def clear_token_usage():
        """Clear the token usage in the framework context."""
        trace_id = FrameworkContextManager().get_context('trace_id')
        if trace_id is not None:
            FrameworkContextManager().del_context(trace_id + '_token_usage')
        FrameworkContextManager().del_context('trace_id')

    @staticmethod
    def get_token_usage():
        """Get the token usage in the framework context."""
        trace_id = FrameworkContextManager().get_context('trace_id')
        return FrameworkContextManager().get_context(trace_id + '_token_usage', {}) if trace_id is not None else {}

    def _get_or_create_subdir(self, subdir: str) -> str:
        """Get or create a subdirectory if it doesn't exist in the monitor directory."""
        path = os.path.join(self.dir, subdir)
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def default_serializer(obj):
        """Default serializer for objects."""
        if isinstance(obj, InputObject):
            return obj.to_dict()
        elif isinstance(obj, OutputObject):
            return obj.to_dict()
        elif isinstance(obj, BaseModel):
            try:
                return obj.dict()
            except TypeError:
                raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
        else:
            raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    def serialize_obj(self, obj):
        """Serialize an object and filter out non-serializable values."""
        filtered_obj = self.filter_and_serialize(obj)
        return json.loads(json.dumps(filtered_obj, default=self.default_serializer))

    def filter_and_serialize(self, obj):
        """Recursively filter out non-serializable values from an object."""

        def is_json_serializable(value):
            """Check if value is a JSON serializable object."""
            try:
                json.dumps(value, default=self.default_serializer)
                return True
            except (TypeError, OverflowError):
                return False

        def filter_dict(d):
            return {k: v for k, v in d.items() if is_json_serializable(v)}

        def recursive_filter(o):
            if isinstance(o, dict):
                return filter_dict({k: recursive_filter(v) for k, v in o.items()})
            elif isinstance(o, list):
                return [recursive_filter(i) for i in o if is_json_serializable(i)]
            else:
                return o

        return recursive_filter(obj)
