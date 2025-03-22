# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2025/03/22 18:15
# @Author  : hiro
# @Email   : hiromesh@qq.com
# @FileName: test_command_status.py

import os
import json
import time
import unittest

from agentuniverse.agent.action.tool.tool import ToolInput
from agentuniverse.agent.action.tool.common_tool.run_command_tool import (
    RunCommandTool,
    CommandStatus,
)
from agentuniverse.agent.action.tool.common_tool.command_status_tool import CommandStatusTool


class CommandStatusToolTest(unittest.TestCase):
    def setUp(self):
        self.run_tool = RunCommandTool()
        self.status_tool = CommandStatusTool()

    def test_command_status_check(self):
        tool_input = ToolInput({
            'command': 'echo "Hello World"',
            'cwd': os.getcwd(),
            'blocking': True
        })
        result_json = self.run_tool.execute(tool_input)
        result = json.loads(result_json)
        thread_id = result['thread_id']
        
        status_input = ToolInput({
            'thread_id': thread_id
        })
        status_json = self.status_tool.execute(status_input)
        status_result = json.loads(status_json)
        
        self.assertEqual(status_result['thread_id'], thread_id)
        self.assertEqual(status_result['status'], CommandStatus.COMPLETED.value)
        self.assertIn('Hello World', status_result['stdout'])
        self.assertEqual(status_result['exit_code'], 0)

    def test_running_command_status(self):
        tool_input = ToolInput({
            'command': 'sleep 2 && echo "Long running command finished"',
            'cwd': os.getcwd(),
            'blocking': False
        })
        result_json = self.run_tool.execute(tool_input)
        result = json.loads(result_json)
        thread_id = result['thread_id']
        
        status_input = ToolInput({
            'thread_id': thread_id
        })
        status_json = self.status_tool.execute(status_input)
        status_result = json.loads(status_json)        
        
        time.sleep(3)
        status_json = self.status_tool.execute(status_input)
        status_result = json.loads(status_json)
        
        self.assertEqual(status_result['status'], CommandStatus.COMPLETED.value)
        self.assertIn('Long running command finished', status_result['stdout'])
        self.assertEqual(status_result['exit_code'], 0)

    def test_invalid_thread_id(self):
        status_input = ToolInput({
            'thread_id': 12345678  # A thread ID that shouldn't exist
        })
        status_json = self.status_tool.execute(status_input)
        status_result = json.loads(status_json)
        
        self.assertIn('error', status_result)
        self.assertEqual(status_result['status'], 'not_found')


if __name__ == '__main__':
    unittest.main()
