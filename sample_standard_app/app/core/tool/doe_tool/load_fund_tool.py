from typing import Optional

import requests
from bs4 import BeautifulSoup

from agentuniverse.agent.action.tool.tool import Tool, ToolInput


class LoadFundInfoTool(Tool):
    fund_info_url: Optional[str] = "https://fund.pingan.com/main/peanutFinance/yingPeanut/fundDetailV2/"

    fund_rate_info_url: Optional[str] = "https://fund.eastmoney.com/"

    def execute(self, tool_input: ToolInput):
        fund_id = tool_input.get_data("fund_id")
        fund_info_url = f"{self.fund_info_url}{fund_id}.shtml"
        # 爬取页面中基金的信息
        response = requests.get(fund_info_url)
        response.encoding = "utf-8"
        html_content = response.text

        rate_info_url = f"{self.fund_rate_info_url}{fund_id}.html"

        response = requests.get(rate_info_url)
        response.encoding = "utf-8"
        rate_html_content = response.text
        soup = BeautifulSoup(rate_html_content, "html.parser")
        elem = soup.find("li", id="increaseAmount_stage").find("table", class_="ui-table-hover")
        html_content = html_content + "\n========================================\n" + str(elem.contents)
        return {
            "init_data": html_content
        }