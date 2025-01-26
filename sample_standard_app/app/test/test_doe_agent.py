# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/10/18 15:25
# @Author  : weizjajj
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: test_doe_agent.py

import unittest

from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.base.agentuniverse import AgentUniverse


class DOEAgentTestCase(unittest.TestCase):
    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    # def test_data_fining_agent(self):
    #     agent_instance = AgentManager().get_instance_obj('data_fining_agent')
    #     res = agent_instance.run(fund_id="000759",input="请帮我总结基金表现")
    #     print(json.dumps(res.to_dict(),ensure_ascii=False))

    # def test_framework_matching_agent(self):
    #     # agent_instance = AgentManager().get_instance_obj('data_fining_agent')
    #     # res = agent_instance.run(fund_id="000759")
    #
    #
    #     fund_info_str = """
    #     {"name": "平安财富宝货币 A", "date": "2024-10-13", "EPTWU": "0.4884", "seven_day_annualized": "1.789%", "since_founding": "35.88%", "base_income_info": {"last_week": "0.05%", "last_month": "0.15%", "last_three_moth": "0.46%", "last_six_moth": "0.96%", "this_year": "1.61%", "last_year": "2.13%"}, "peer_income_info": {"last_week": "0.04%", "last_month": "0.10%", "last_three_moth": "0.23%", "last_six_moth": "0.57%", "this_year": "1.24%", "last_year": "1.73%"}, "CSI_300": {"last_week": "-3.25%", "last_month": "22.00%", "last_three_moth": "12.08%", "last_six_moth": "10.93%", "this_year": "13.29%", "last_year": "5.99%"}, "ranker": {"last_week": "82 | 895", "last_month": "52 | 894", "last_three_moth": "24 | 886", "last_six_moth": "27 | 878", "this_year": "25 | 855", "last_year": "26 | 834"}, "manager_info": {"name": "罗薇", "date": "2020-11-01", "description": "罗薇女士，新南威尔士大学金融会计学专业硕士，曾任红塔红土基金管理有限公司固定收益交易员、基金经理助理、基金经理。2020年11月加入平安基金管理有限公司，现任平安交易型货币市场基金（2022-05-24至今）、平安日增利货币市场基金（2022-06-13至今）、平安合丰定期开放纯债债券型发起式证券投资基金（2022-06-17至今）、平安惠鸿纯债债券型证券投资基金（2022-07-01至今）、平安合慧定期开放纯债债券型发起式证券投资基金（2022-07-01至今）、平安惠隆纯债债券型证券投资基金（2022-07-01至今）、平安惠兴纯债债券型证券投资基金（2022-07-01至今）、平安财富宝货币市场基金（2022-07-01至今）、平安惠信3个月定期开放债券型证券投资基金（2022-11-07至今）基金经理。"}, "risk_rating": "low", "investment_scope": "本基金投资于法律法规及监管机构允许投资的金融工具，包括现金，通知存款，短期融资券，一年以内（含一年）的银行定期存款、大额存单，期限在一年以内（含一年）的债券回购，期限在一年以内（含一年）的中央银行票据，剩余期限在397天以内（含397天）的债券、资产支持证券、中期票据，中国证监会及/或中国人民银行认可的其他具有良好流动性的金融工具。", "risk_return_profile": "本基金为货币市场基金，是证券投资基金中的低风险品种。本基金的风险和预期收益低于股票型基金、混合型基金、债券型基金。", "funding_time": "2014-08-21", "funding_rating": {"manage_rating": "0.0015", "custodial_fee": "0.0005", "annual_sales_service_fee": "0.0001", "subscription_fee": "0", "redemption_fee": "0"}, "asset_allocation": {"stocks": "0.00%", "fund_investment": "0.00%", "fixed_income_investment": "40.18%", "precious_metals_investment": "0.00%", "financial_derivatives_investment": "0.00%", "repurchase_agreements": "16.13%", "bank_deposits": "43.46%", "settlement_reserve": "0.00%", "others": "0.24%"}, "net_asset_value": [{"date": "2024-10-13", "EPTWU": "0.4884", "seven_day_annualized": "1.789%"}]}
    #     """
    #
    #     fund_info = json.loads(fund_info_str)
    #
    #     # print(json.dumps(fund_info,ensure_ascii=False))
    #
    #
    #     tool:Tool = ToolManager().get_instance_obj('load_framework_tool')
    #
    #     frameworks = tool.run(framework_path = "./doe_data/framework.csv")
    #     print(frameworks)
    #
    #     agent_instance:Agent = AgentManager().get_instance_obj('framework_matching_agent')
    #
    #     res = agent_instance.run(fund_info=fund_info, frameworks=frameworks)
    #     print(res.to_dict().get('output'))

    #     def test_json_output_parser_tool(self):
    #         data = """
    #         ```json
    # {
    #   "thought": "平安财富宝货币 A 是一款货币市场基金，其主要投资于低风险的金融工具，如银行存款、短期债券等。其风险评级为低，表明其风险和预期收益都较低。基金的收益率和同类基金相比表现较好，且基金经理具有丰富的固定收益投资经验，投资风格稳定。",
    #   "product_track": "均衡风格",
    #   "interpret_latitude": "持续超额收益能力",
    #   "argument_direction": "正",
    #   "argument_direction_list": ["持续超额能力强", "风控能力较强"],
    #   "expression_techniques": "持续超额收益能力强"
    # }
    # ```
    #         """
    #
    #         tool = ToolManager().get_instance_obj('json_output_parser_tool')
    #         res = tool.run(output=data)
    #         print(res)

    # def test_opinion_inject_agent(self):
    #     fund_info_str = """
    #            {"name": "平安财富宝货币 A", "last_six_month": 0.02, "manager_year":3, "date": "2024-10-13", "EPTWU": "0.4884", "seven_day_annualized": "1.789%", "since_founding": "35.88%", "base_income_info": {"last_week": "0.05%", "last_month": "0.15%", "last_three_moth": "0.46%", "last_six_moth": "0.96%", "this_year": "1.61%", "last_year": "2.13%"}, "peer_income_info": {"last_week": "0.04%", "last_month": "0.10%", "last_three_moth": "0.23%", "last_six_moth": "0.57%", "this_year": "1.24%", "last_year": "1.73%"}, "CSI_300": {"last_week": "-3.25%", "last_month": "22.00%", "last_three_moth": "12.08%", "last_six_moth": "10.93%", "this_year": "13.29%", "last_year": "5.99%"}, "ranker": {"last_week": "82 | 895", "last_month": "52 | 894", "last_three_moth": "24 | 886", "last_six_moth": "27 | 878", "this_year": "25 | 855", "last_year": "26 | 834"}, "manager_info": {"name": "罗薇", "date": "2020-11-01", "description": "罗薇女士，新南威尔士大学金融会计学专业硕士，曾任红塔红土基金管理有限公司固定收益交易员、基金经理助理、基金经理。2020年11月加入平安基金管理有限公司，现任平安交易型货币市场基金（2022-05-24至今）、平安日增利货币市场基金（2022-06-13至今）、平安合丰定期开放纯债债券型发起式证券投资基金（2022-06-17至今）、平安惠鸿纯债债券型证券投资基金（2022-07-01至今）、平安合慧定期开放纯债债券型发起式证券投资基金（2022-07-01至今）、平安惠隆纯债债券型证券投资基金（2022-07-01至今）、平安惠兴纯债债券型证券投资基金（2022-07-01至今）、平安财富宝货币市场基金（2022-07-01至今）、平安惠信3个月定期开放债券型证券投资基金（2022-11-07至今）基金经理。"}, "risk_rating": "low", "investment_scope": "本基金投资于法律法规及监管机构允许投资的金融工具，包括现金，通知存款，短期融资券，一年以内（含一年）的银行定期存款、大额存单，期限在一年以内（含一年）的债券回购，期限在一年以内（含一年）的中央银行票据，剩余期限在397天以内（含397天）的债券、资产支持证券、中期票据，中国证监会及/或中国人民银行认可的其他具有良好流动性的金融工具。", "risk_return_profile": "本基金为货币市场基金，是证券投资基金中的低风险品种。本基金的风险和预期收益低于股票型基金、混合型基金、债券型基金。", "funding_time": "2014-08-21", "funding_rating": {"manage_rating": "0.0015", "custodial_fee": "0.0005", "annual_sales_service_fee": "0.0001", "subscription_fee": "0", "redemption_fee": "0"}, "asset_allocation": {"stocks": "0.00%", "fund_investment": "0.00%", "fixed_income_investment": "40.18%", "precious_metals_investment": "0.00%", "financial_derivatives_investment": "0.00%", "repurchase_agreements": "16.13%", "bank_deposits": "43.46%", "settlement_reserve": "0.00%", "others": "0.24%"}, "net_asset_value": [{"date": "2024-10-13", "EPTWU": "0.4884", "seven_day_annualized": "1.789%"}]}
    #            """
    #     fund_info = json.loads(fund_info_str)
    #     framework_path = "./doe_data/opinions.csv"
    #     agent_instance: Agent = AgentManager().get_instance_obj('opinion_inject_agent')
    #     res = agent_instance.run(input="请帮我生成一个基金解读报告", data_fining_result=fund_info,
    #                              opinions_path=framework_path)
    #     print(res.to_dict())

    def test_doe_agent(self):
        fund_id = "009008"
        framework_path = "./doe_data/opinions.csv"
        agent = AgentManager().get_instance_obj('doe_agent_case')
        res = agent.run(fund_id=fund_id, opinions_path=framework_path,input="请给出基金近期表现的研究报告",business_scene="基金分析")
        print(res.to_dict().get('output'))


if __name__ == '__main__':
    unittest.main()
