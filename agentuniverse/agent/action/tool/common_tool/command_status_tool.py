# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2025/3/22 18:00
# @Author  : hiro
# @Email   : hiromesh@qq.com
# @FileName: command_status_tool.py

import json
from agentuniverse.agent.action.tool.tool import Tool, ToolInput
from agentuniverse.agent.action.tool.common_tool.run_command_tool import get_command_result


class CommandStatusTool(Tool):
    def execute(self, tool_input: ToolInput) -> str:
        thread_id = tool_input.get_data("thread_id")

        if isinstance(thread_id, str) and thread_id.isdigit():
            thread_id = int(thread_id)

        result = get_command_result(thread_id)

        if result is None:
            return json.dumps({
                "error": f"No command found with thread_id: {thread_id}",
                "status": "not_found"
            })
        return result.message
