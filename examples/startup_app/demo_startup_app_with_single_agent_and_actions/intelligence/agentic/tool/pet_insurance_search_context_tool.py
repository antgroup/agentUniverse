# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/11/12 11:59
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: search_context_tool.py
import json

from agentuniverse.agent.action.tool.tool import Tool, ToolInput
from agentuniverse.base.util.logging.logging_util import LOGGER

# Mock API http url.
API_URL = "www.xxxx.com/query_knowledge"


class MockAPI:
    """Mock API 请求逻辑"""

    def post(self, url, headers, data):
        # mock response
        mock_response = {
            "result": {
                "recallResultTuples": [
                    {
                        "knowledgeTitle": "mock data: 宠物医保升级规则",
                        "content": "宠物医保在保障期间暂不支持升级。宠物医保有基础版、升级版、尊享版三个版本，投保某一版本后不支持升级为别的版本。"
                                   "如果您希望享受更高级别的保障，可以在当前保险期结束后，重新选择更高版本的宠物医保进行投保。例如，从基础版升级到升级版或尊享版。"
                    },
                    {
                        "knowledgeTitle": "mock data: 宠物医保（体验版）简介",
                        "content": "宠物医保（体验版）是免费体验版，仅有30天保障时间。宠物医保（体验版）体验30天后付费可升级成宠物医保升级版。"
                    },
                    {
                        "knowledgeTitle": "mock data: 宠物医保简介",
                        "content": "宠物医保保障期限12个月，是付费版商业险，有三个保障：基础版、升级版、尊享版。"
                    },
                ]
            }
        }
        return MockResponse(mock_response)


class MockResponse:
    """Mock API http response."""

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class SearchContextTool(Tool):
    """"
    SearchContextTool是一个企业内部知识检索api工具示例，通过在tool的execute执行方法中拼接http header&request，向特定endpoint发起检索请求，拿到返回结果后拼接为自然语言形式response作为模型上下文。

    当前通过MOCK_URL(www.xxxx.com/query_knowledge)和MOCK_API的请求和返回结果做工具检索样例展示。
    """

    def execute(self, tool_input: ToolInput):
        question = tool_input.get_data('input')
        try:
            headers = {
                "Content-Type": "application/json"
            }
            # 要发送的数据
            data = {
                "chatId": "xxxx",
                "sessionId": "xxxx",
                "userId": "xxxxx",
                "sceneCode": "xxxx",
                "query": question,
                "decoderType": "xxxx",
                "inputMethod": "user_input",
                "enterScene": {
                    "sceneCode": "xxx",
                    "productNo": "xxxx",
                }
            }
            # 检索数据top_k
            top_k = tool_input.get_data('top_k') if tool_input.get_data('top_k') else 2
            LOGGER.info(f"search context tool input: {data}")
            # 请求mock api，真实场景请求http request.
            response = MockAPI().post(API_URL, headers=headers, data=json.dumps(data, ensure_ascii=False))
            # 解析http response.
            result = response.json()['result']
            recallResultTuples = result.get('recallResultTuples')
            # 拼装检索信息.
            context = f"提出的问题是:{question}\n\n这个问题检索到的答案相关内容是:\n\n"
            index = 0
            for recallResult in recallResultTuples:
                if index == top_k:
                    return context
                if recallResult.get('content'):
                    context += (f"knowledgeTitle: {recallResult.get('knowledgeTitle')}\n"
                                f"knowledgeContent: {recallResult.get('content')}\n\n")
                    index += 1
            # return final search context.
            return context
        except Exception as e:
            LOGGER.error(f"invoke search context tool failed: {str(e)}")
            raise e
