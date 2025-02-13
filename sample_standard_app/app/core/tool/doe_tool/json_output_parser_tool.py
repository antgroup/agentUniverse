from langchain_core.utils.json import parse_json_markdown

from agentuniverse.agent.action.tool.tool import Tool, ToolInput


class JsonOutputParser(Tool):
    def execute(self, tool_input: ToolInput):
        json_str = tool_input.get_data("output")
        res = parse_json_markdown(json_str)
        return {
            "output": res
        }
