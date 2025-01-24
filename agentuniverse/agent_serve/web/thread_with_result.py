# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/3/26 14:31
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: thread_with_result.py

import threading
from threading import Thread
import weakref
from concurrent.futures.thread import ThreadPoolExecutor, _worker, _threads_queues

from agentuniverse.base.context.framework_context_manager import FrameworkContextManager


class ThreadWithReturnValue(Thread):
    """A thread can save the target func exec result."""

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        super().__init__(group, target, name, args, kwargs)

        if kwargs is None:
            kwargs = {}
        self.kwargs = kwargs
        self.args = args
        self.target = target
        self._return = None
        self.error = None
        self._context_values: dict = FrameworkContextManager().get_all_contexts()

    def run(self):
        """Run the target func and save result in _return."""
        if self.target is not None:
            context_tokens = {}
            # set the context values in the thread
            for var_name, var_value in self._context_values.items():
                token = FrameworkContextManager().set_context(var_name, var_value)
                context_tokens[var_name] = token

            try:
                self._return = self.target(*self.args, **self.kwargs)
            except Exception as e:
                self.error = e
            finally:
                if 'output_stream' in self.kwargs:
                    self.kwargs['output_stream'].put('{"type": "EOF"}')
                # finally, clear the context values in the thread
                for var_name, token in context_tokens.items():
                    FrameworkContextManager().reset_context(var_name, token)

    def result(self):
        """Wait for target func finished, then return the result or raise an
        error."""
        self.join()
        if self.error is not None:
            raise self.error
        return self._return


class ThreadPoolExecutorWithReturnValue(ThreadPoolExecutor):
    def _adjust_thread_count(self):
        # if idle threads are available, don't spin new threads
        if self._idle_semaphore.acquire(timeout=0):
            return

        # When the executor gets lost, the weakref callback will wake up
        # the worker threads.
        def weakref_cb(_, q=self._work_queue):
            q.put(None)

        num_threads = len(self._threads)
        if num_threads < self._max_workers:
            thread_name = '%s_%d' % (self._thread_name_prefix or self,
                                     num_threads)
            t = ThreadWithReturnValue(name=thread_name, target=_worker,
                                 args=(weakref.ref(self, weakref_cb),
                                       self._work_queue,
                                       self._initializer,
                                       self._initargs))
            t.start()
            self._threads.add(t)
            _threads_queues[t] = self._work_queue