# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/6/5 15:33
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: trace.py
import asyncio
import functools
import inspect

from functools import wraps

from agentuniverse.base.context.framework_context_manager import FrameworkContextManager
from agentuniverse.base.util.monitor.monitor import Monitor
from agentuniverse.llm.llm_output import LLMOutput


def trace_llm(func):
    """Annotation: @trace_llm

    Decorator to trace the LLM invocation, add llm input and output to the monitor.
    """

    @wraps(func)
    async def wrapper_async(*args, **kwargs):
        # get llm input from arguments
        llm_input = _get_llm_input(func, *args, **kwargs)

        source = func.__qualname__

        # check whether the tracing switch is enabled
        self = llm_input.pop('self', None)

        if self and hasattr(self, 'name'):
            name = self.name
            if name is not None:
                source = name

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'llm'})

        if self and hasattr(self, 'tracing'):
            if self.tracing is False:
                return await func(*args, **kwargs)

        # invoke function
        result = await func(*args, **kwargs)
        # not streaming
        if isinstance(result, LLMOutput):
            # add llm invocation info to monitor
            Monitor().trace_llm_invocation(source=func.__qualname__, llm_input=llm_input, llm_output=result.text)
            return result
        else:
            # streaming
            async def gen_iterator():
                llm_output = []
                async for chunk in result:
                    llm_output.append(chunk.text)
                    yield chunk
                # add llm invocation info to monitor
                Monitor().trace_llm_invocation(source=func.__qualname__, llm_input=llm_input,
                                               llm_output="".join(llm_output))

            return gen_iterator()

    @functools.wraps(func)
    def wrapper_sync(*args, **kwargs):

        # get llm input from arguments
        llm_input = _get_llm_input(func, *args, **kwargs)

        source = func.__qualname__

        # check whether the tracing switch is enabled
        self = llm_input.pop('self', None)
        if self and hasattr(self, 'name'):
            name = self.name
            if name is not None:
                source = name

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'llm'})

        if self and hasattr(self, 'tracing'):
            if self.tracing is False:
                return func(*args, **kwargs)

        # invoke function
        result = func(*args, **kwargs)
        # not streaming
        if isinstance(result, LLMOutput):
            # add llm invocation info to monitor
            Monitor().trace_llm_invocation(source=func.__qualname__, llm_input=llm_input, llm_output=result.text)

            # add llm token usage to monitor
            trace_llm_token_usage(self, llm_input, result.text)

            return result
        else:
            # streaming
            def gen_iterator():
                llm_output = []
                for chunk in result:
                    llm_output.append(chunk.text)
                    yield chunk

                output_str = "".join(llm_output)

                # add llm invocation info to monitor
                Monitor().trace_llm_invocation(source=func.__qualname__, llm_input=llm_input,
                                               llm_output=output_str)

                # add llm token usage to monitor
                trace_llm_token_usage(self, llm_input, output_str)

            return gen_iterator()

    if asyncio.iscoroutinefunction(func):
        # async function
        return wrapper_async
    else:
        # sync function
        return wrapper_sync


def _get_llm_input(func, *args, **kwargs) -> dict:
    """Get the llm input from arguments."""
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    return {k: v for k, v in bound_args.arguments.items()}


def trace_agent(func):
    """Annotation: @trace_agent

    Decorator to trace the agent invocation, add agent input and output to the monitor.
    """

    @functools.wraps(func)
    async def wrapper_async(*args, **kwargs):
        # get agent input from arguments
        agent_input = _get_input(func, *args, **kwargs)
        # check whether the tracing switch is enabled
        source = func.__qualname__
        self = agent_input.pop('self', None)

        tracing = None
        if isinstance(self, object):
            agent_model = getattr(self, 'agent_model', None)
            if isinstance(agent_model, object):
                info = getattr(agent_model, 'info', None)
                profile = getattr(agent_model, 'profile', None)
                if isinstance(info, dict):
                    source = info.get('name', None)
                if isinstance(profile, dict):
                    tracing = profile.get('tracing', None)

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'agent'})

        if tracing is False:
            return await func(*args, **kwargs)

        # invoke function
        result = await func(*args, **kwargs)
        # add agent invocation info to monitor
        Monitor().trace_agent_invocation(source=source, agent_input=agent_input, agent_output=result)
        return result

    @functools.wraps(func)
    def wrapper_sync(*args, **kwargs):
        # get agent input from arguments
        agent_input = _get_input(func, *args, **kwargs)
        # check whether the tracing switch is enabled
        source = func.__qualname__
        self = agent_input.pop('self', None)

        tracing = None
        if isinstance(self, object):
            agent_model = getattr(self, 'agent_model', None)
            if isinstance(agent_model, object):
                info = getattr(agent_model, 'info', None)
                profile = getattr(agent_model, 'profile', None)
                if isinstance(info, dict):
                    source = info.get('name', None)
                if isinstance(profile, dict):
                    tracing = profile.get('tracing', None)

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'agent'})

        if tracing is False:
            return func(*args, **kwargs)

        # invoke function
        result = func(*args, **kwargs)
        # add agent invocation info to monitor
        Monitor().trace_agent_invocation(source=source, agent_input=agent_input, agent_output=result)
        return result

    if asyncio.iscoroutinefunction(func):
        # async function
        return wrapper_async
    else:
        # sync function
        return wrapper_sync


def trace_tool(func):
    """Annotation: @trace_tool

    Decorator to trace the tool invocation.
    """

    @functools.wraps(func)
    def wrapper_sync(*args, **kwargs):
        # get tool input from arguments
        tool_input = _get_input(func, *args, **kwargs)

        source = func.__qualname__
        self = tool_input.pop('self', None)

        if isinstance(self, object):
            name = getattr(self, 'name', None)
            if name is not None:
                source = name

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'tool'})

        # invoke function
        return func(*args, **kwargs)

    # sync function
    return wrapper_sync


def trace_knowledge(func):
    """Annotation: @trace_knowledge

    Decorator to trace the knowledge invocation.
    """

    @functools.wraps(func)
    def wrapper_sync(*args, **kwargs):
        # get knowledge input from arguments
        knowledge_input = _get_input(func, *args, **kwargs)

        source = func.__qualname__
        self = knowledge_input.pop('self', None)

        if isinstance(self, object):
            name = getattr(self, 'name', None)
            if name is not None:
                source = name

        # add invocation chain to the monitor module.
        Monitor.add_invocation_chain({'source': source, 'type': 'knowledge'})

        # invoke function
        return func(*args, **kwargs)

    # sync function
    return wrapper_sync


def _get_input(func, *args, **kwargs) -> dict:
    """Get the agent input from arguments."""
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    return {k: v for k, v in bound_args.arguments.items()}


def _get_llm_token_usage(llm_obj: object, llm_input: dict, output_str: str) -> dict:
    """ Calculate the token usage of the given LLM object.
    Args:
        llm_obj(object): LLM object.
        llm_input(dict): Dictionary of LLM input.
        output_str(str): LLM output.

    Returns:
        dict: Dictionary of token usage including the completion_tokens, prompt_tokens, and total_tokens.
    """
    try:
        if llm_obj is None or llm_input is None:
            return {}
        messages = llm_input.get('kwargs', {}).pop('messages', None)

        input_str = ''
        if messages is not None and isinstance(messages, list):
            for m in messages:
                if isinstance(m, dict):
                    input_str += str(m.get('role', '')) + '\n'
                    input_str += str(m.get('content', '')) + '\n'

                elif isinstance(m, object):
                    if hasattr(m, 'role'):
                        role = m.role
                        if role is not None:
                            input_str += str(m.role) + '\n'
                    if hasattr(m, 'content'):
                        content = m.content
                        if content is not None:
                            input_str += str(m.content) + '\n'

        if input_str == '' or output_str == '':
            return {}

        usage = {}
        # the number of input and output tokens is calculated by the llm `get_num_tokens` method.
        if hasattr(llm_obj, 'get_num_tokens'):
            completion_tokens = llm_obj.get_num_tokens(output_str)
            prompt_tokens = llm_obj.get_num_tokens(input_str)
            total_tokens = completion_tokens + prompt_tokens
            usage = {'completion_tokens': completion_tokens, 'prompt_tokens': prompt_tokens,
                     'total_tokens': total_tokens}
        return usage
    except Exception as e:
        return {}


def trace_llm_token_usage(llm_obj: object, llm_input: dict, output_str: str) -> None:
    """ Trace the token usage of the given LLM object.
    Args:
        llm_obj(object): LLM object.
        llm_input(dict): Dictionary of LLM input.
        output_str(str): LLM output.
    """
    trace_id = FrameworkContextManager().get_context('trace_id')
    # trace token usage for a complete request chain based on trace id
    if trace_id:
        token_usage: dict = _get_llm_token_usage(llm_obj, llm_input, output_str)
        if token_usage:
            Monitor.add_token_usage(token_usage)
