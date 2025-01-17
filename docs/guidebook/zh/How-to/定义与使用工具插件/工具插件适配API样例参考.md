# Bing并发搜索api
## api接口描述
使用该工具可以在bing中并发检索多条信息。

bing搜索需要[https://www.searchapi.io/](https://www.searchapi.io/)申请相应的api_key。该工具基于单个问题检索实现了并发多信息检索。

## 输入描述
入参inputs是一个json字符串，内容是一个待检索list，每个元素表示一条需要搜索的信息。

```json
["贝多芬 交响乐", "肖邦 随想曲", "舒伯特 夜曲"]
```

## 输出描述
输出是对每个检索问题和结果的封装，以“--------------------------”隔开，格式如下

```text
query: 贝多芬 交响乐
result: 世界音乐史上最伟大交响曲的缔造，被誉为“乐圣”的贝多芬，其一生中所创作的九大交响曲，“无人能望其项背”。其中有三首被世界纳入世界音乐史最伟大的十首交响曲之中，其余六首也在世界交响曲排名中名列前茅。
--------------------------
query: 肖邦 随想曲
result: E大调随想曲是肖邦作品中最著名的一首，也是浪漫时期钢琴曲中的代表之一。
-------------------------
query: 舒伯特 夜曲
result: 《舒伯特小夜曲》是奥地利作曲家舒伯特（1797-1828）创作的歌曲，他在欧洲音乐史上有“歌曲之王”的称誉。当时的民间传说认为，天鹅将死的时候，会唱出最动人的歌。
```

## AU中封装该api工具
**yaml配置**

```yaml
name: 'parallel_search_detail_api'
description: |
  使用该工具可以在bing中并发搜索多条信息
    <输入描述>
    入参inputs是一个json字符串，内容是一个待检索list，每个元素表示一条需要搜索的信息。
    
    <输出描述>
    输出是对每个检索问题和结果的封装，以“--------------------------”隔开。
    query: xxx
    result: xxx
    -------------------------
    query: xxx
    result: xxx
    -------------------------
    
    <工具输入示例>
      你想要搜索信息，如不同的几位音乐家的作品，且不需要返回详细结果的话，工具的输入应该是: 
        ["贝多芬 交响乐", "肖邦 随想曲", "舒伯特 夜曲"]
        
    <工具输出示例>
      工具的输出应该是: 
        query: 贝多芬 交响乐
        result: 世界音乐史上最伟大交响曲的缔造，被誉为“乐圣”的贝多芬，其一生中所创作的九大交响曲，“无人能望其项背”。其中有三首被世界纳入世界音乐史最伟大的十首交响曲之中，其余六首也在世界交响曲排名中名列前茅。
        --------------------------
        query: 肖邦 随想曲
        result: E大调随想曲是肖邦作品中最著名的一首，也是浪漫时期钢琴曲中的代表之一。
        -------------------------
        query: 舒伯特 夜曲
        result: 《舒伯特小夜曲》是奥地利作曲家舒伯特（1797-1828）创作的歌曲，他在欧洲音乐史上有“歌曲之王”的称誉。当时的民间传说认为，天鹅将死的时候，会唱出最动人的歌。
      
tool_type: 'api'
input_keys: ['inputs']
metadata:
  type: 'TOOL'
  module: 'au_expert_assistant.intelligence.agentic.tool.search.parallel_search_detail_api'
  class: 'ParallelSearchDetailApi'
```

**代码实现参考**

```text
class ParallelSearchDetailApi(ZxzTool):
    async def execute(self, tool_input: ToolInput):
        try:
            json_input = tool_input.get_data("input")
            json_input = parse_and_check_json_markdown(json_input, ["input_params", "save_params"])
            query_list = json_input['input_params'].get('query', [])
            search_tool = ToolManager().get_instance_obj('knowledge_search_detail_api')

            executor_res = await asyncio.gather(
                *[search_tool.run(
                    query=query,
                    search_top=3
                ) for query in query_list]
            )
            result_str = ''

            for res in executor_res:
                result_str += f'query:' + res['query'] + '\n'
                result_str += f'result:' + res['search_results'][0] + '\n'
                result_str += '--------------------------\n'

            update_react_memory(
                name=json_input["save_params"]["name"],
                data=result_str,
                description=json_input["save_params"]["description"]
            )
            if json_input["save_params"].get("full_return"):
                return result_str
            return '执行成功，可继续下一步'
        except Exception as e:
            error_message = traceback.format_exc()
            return error_message

```

# 谷歌酒店搜索api
## api接口描述
该api调用谷歌的开放api接口 https://serpapi.com/search 中的google_hotels引擎服务查询酒店相关信息（该接口需要去谷歌api开放官网申请相应的api-key即可访问）。

## 输入描述
工具的输入input为json_markdown格式的字符串，内容是下面的结构

```json
{
  "input_params": {
    "query": "怡莱酒店南昌胜利路步行街店",
    "check_in_date": "2024-11-24",
    "check_out_date": "2024-11-25",
    "search_type": "name",
    "hotel_class": 3    
  },
  "save_params":{
    "name": "怡莱酒店南昌胜利路步行街店",
    "description":"记载了怡莱酒店南昌胜利路步行街店的具体住宿信息",
    "full_return": false
  }
}
```

**必选参数：**

query：可以是具体酒店名称或者地名，注意地名只能是巴黎、南昌这种地名。这个工具不支持复杂的搜索如巴黎民宿、南昌高档酒店

search_type：有两种取值location和name，当query是具体酒店名称时，该取值为name，地名的话则是location。

check_in_date和check_out_date为YYYY-MM-DD格式的入住和离店日期

**可选参数：**

hotel_class取值为范围为2-5表示酒店档次。

min_price和max_price表示筛选的价格区间，但min_price和max_price取值不能为0。

save_params参数：用于将最后结果归档。save_params包含三个属性，归档名称name和结果内容的简要描述description以及是否表示需要返回完整结果的full_return

## 输出描述
输出为json字符串，内容为检索到的hotel信息列表，按匹配度从高到低排列，每个hotel结构包含描述，链接，地址，联系方式，图片，定位，价格等信息。下面为示例：

```json
[{
  "type": "hotel",
  "name": "怡莱酒店（南昌胜利路步行街店）",
  "description": "怡莱酒店（南昌胜利路步行街店）位于南昌繁华市中心步行街建德观街，门即是中山路——胜利路步行街，门前是南昌知名小吃夜宵街——建德观街；紧靠八一大桥，距江南三大名...",
  "link": "https://www.h10hotels.com/en/barcelona-hotels/h10-port-vell?utm_source=google_my_business&utm_medium=boton_sitio_web&utm_campaign=hpv",
  "address": "0791-82075888",
  "phone": "+34 933 10 30 65",
  "phone_link": "tel:+34933103065",
  "gps_coordinates": {
    "latitude": 41.381571799999996,
    "longitude": 2.1838414999999998
  },
  "check_in_time": "3:00 PM",
  "check_out_time": "12:00 PM",
  "rate_per_night": {
    "lowest": "$123",
    "extracted_lowest": 123,
    "before_taxes_fees": "$100",
    "extracted_before_taxes_fees": 100
  },
  "total_rate": {
    "lowest": "$123",
    "extracted_lowest": 123,
    "before_taxes_fees": "$100",
    "extracted_before_taxes_fees": 100
  }
}]
```

## AU中封装该api工具
```yaml
name: 'hotel_search_api'
description: '使用该工具可以搜索酒店相关的信息。
    <输入描述>
    query可以是具体酒店名称或者地名，注意地名只能是巴黎、南昌这种地名。这个工具不支持复杂的搜索如巴黎民宿、南昌高档酒店
    search_type有两种取值location和name，当query是具体酒店名称时，该取值为name，地名的话则是location。
    check_in_date和check_out_date为YYYY-MM-DD格式的入住和离店日期
    可选参数：
      hotel_class取值为范围为2-5表示酒店档次。
      min_price和max_price表示筛选的价格区间，但min_price和max_price取值不能为0。
    同时你也应当提供一个save_params参数，用于将最后结果归档。save_params包含三个属性，归档名称name和结果内容的简要描述description以及是否表示需要返回完整结果的full_return
    
    <输出描述>
    输出为json字符串，内容为检索到的hotel信息列表，按匹配度从高到低排列，每个hotel结构包含描述，链接，地址，联系方式，图片，定位，价格等信息。
    
    <工具输入示例>
      你想要搜索指定酒店住宿信息时如怡莱酒店南昌胜利路步行街店，2024-11-24到2024-11-25的房间信息，且不需要返回详细结果的话，工具的输入应该是: 
        ```json
        {
          "input_params": {
              "query": "怡莱酒店南昌胜利路步行街店",
              "check_in_date": "2024-11-24",
              "check_out_date": "2024-11-25",
              "search_type": "name",
              "hotel_class": 3    
          },
          "save_params":{
            "name": "怡莱酒店南昌胜利路步行街店",
            "description":"记载了怡莱酒店南昌胜利路步行街店的具体住宿信息",
            "full_return": false
          }
        }
        ```
    <工具输出示例>
      返回莱酒店南昌胜利路步行街店的检索结果为：
      [{
        "type": "hotel",
        "name": "怡莱酒店（南昌胜利路步行街店）",
        "description": "怡莱酒店（南昌胜利路步行街店）位于南昌繁华市中心步行街建德观街，门即是中山路——胜利路步行街，门前是南昌知名小吃夜宵街——建德观街；紧靠八一大桥，距江南三大名..."
        "link": "https://www.h10hotels.com/en/barcelona-hotels/h10-port-vell?utm_source=google_my_business&utm_medium=boton_sitio_web&utm_campaign=hpv",
        "address": "0791-82075888",
        "phone": "+34 933 10 30 65",
        "phone_link": "tel:+34933103065",
        "gps_coordinates": {
          "latitude": 41.381571799999996,
          "longitude": 2.1838414999999998
        },
        "check_in_time": "3:00 PM",
        "check_out_time": "12:00 PM",
        "rate_per_night": {
          "lowest": "$123",
          "extracted_lowest": 123,
          "before_taxes_fees": "$100",
          "extracted_before_taxes_fees": 100
        },
        "total_rate": {
          "lowest": "$123",
          "extracted_lowest": 123,
          "before_taxes_fees": "$100",
          "extracted_before_taxes_fees": 100
        }
      }]
    '
tool_type: 'api'
input_keys: ['input']
metadata:
  type: 'TOOL'
  module: 'au_expert_assistant.intelligence.agentic.tool.search.hotel_search_api'
  class: 'HotelSearchApi'
```

**代码实现参考**

```text
class HotelSearchApi(Tool):
    api_key: Optional[str] = Field(
        default_factory=lambda: get_from_env("TOUR_SERP_API_KEY"))
    base_url: str = "https://serpapi.com/search"

    async def request_serpapi(self, url, name, check_in_date, check_out_date, **kwargs):
        language_version = FrameworkContextManager().get_context(
            "language_version")
        params = {
            "engine": "google_hotels",
            "q": name,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "currency": "CNY" if language_version == "cn" else "USD",
            "gl": "cn",
            "hl": "zh-CN" if language_version == "cn" else "en",
            "api_key": self.api_key,
            **kwargs
        }
        for i in range(3):
            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.get(url, params=params)
                    return json.loads(response.text)
            except Exception as e:
                print(e)
        return {'properties':[]}
    async def execute(self, tool_input: ToolInput):
        try:
            json_input = tool_input.get_data("input")
            json_input = parse_and_check_json_markdown(json_input, ["input_params", "save_params"])

            # 先获取酒店详细信息链接
            current_date = datetime.now()
            current_date = current_date.strftime("%Y-%m-%d")
            search_type = json_input["input_params"].pop('search_type')
            if search_type == 'name':
                json_input["input_params"].pop('hotel_class', None)
            if 'min_price' in json_input["input_params"]:
                json_input["input_params"]['min_price'] += 1
            check_in_date = json_input["input_params"].pop('check_in_date', current_date)
            check_in_date = check_in_date if check_in_date > current_date else current_date
            check_out_date = json_input["input_params"].pop('check_out_date', current_date)
            check_out_date = check_out_date if check_out_date > current_date else current_date

            result_dict = await self.request_serpapi(
                self.base_url,
                json_input["input_params"].pop('query'),
                check_in_date,
                check_out_date,
                **json_input["input_params"]
            )
            hotel_details = []

            keys = ['name', 'nearby_places', 'total_rate', 'amenities',
                    'excluded_amenities', "prices", "rate_per_night"]
            if not 'properties' in result_dict:
                print(result_dict)
                return "无相关酒店信息"
            for hotel in result_dict['properties']:
                if hotel['type'] in ['hotel', 'vacation rental'] and 'total_rate' in hotel and 'serpapi_property_details_link' in hotel:
                    hotel_details.append({key: hotel[key] for key in keys if key in hotel})
                    if search_type == 'name':
                        break
                    elif len(hotel_details)>7:
                        break

            if not hotel_details:
                return "无相关酒店信息"

            result_str = json.dumps(hotel_details, ensure_ascii=False)

            update_react_memory(
                name=json_input["save_params"]["name"],
                data=result_str,
                description=json_input["save_params"]["description"]
            )
            if json_input["save_params"].get("full_return"):
                return result_str
            return '执行成功，可继续下一步'
        except Exception as e:
            error_message = traceback.format_exc()
            return error_message

```

# 自定义api-宠物险咨询检索工具
## api接口描述
基于ES自建索引实现对宠物险产品相关问题答案的检索。只针对“宠物医保”及“宠物医保（体验版）”产品有效。

## 输入描述
入参input为待检索的问题

```text
“宠物医保”如何从基础版升级到尊享版？
```

## 输出描述
输出包含“提出的问题”以及“检索到的答案”两部分内容

```plain
提出的问题是:宠物医保投保对宠物年龄的要求是多少？

这个问题检索到的答案相关内容是:
knowledgeTitle: 多大年龄可以投保
knowledgeContent: <p>宠物医保这款产品的投、被保险人为具备完全民事行为的个人，且须为同一人，本产品仅限宠物主本人购买，其承保的宠物须为被保险人以玩赏、陪伴为目的而合法饲养的、可明确鉴别身份的年龄为60天-10周岁的犬类或猫类宠物。</p>

```

检索答案包含knowledgeTitle和knowledgeContent，分别代表检索的知识标题和内容，最终回答一般取knowledgeContent即可。

## AU中封装该api工具
**yaml配置**

```yaml
name: 'pet_insurance_search_context_tool'
description: |
  #工具名称：宠物险产品信息检索工具
  
  #功能描述：提供宠物险产品相关问题答案的检索。只针对“宠物医保”及“宠物医保（体验版）”产品有效。
  
  #工具输入：待检索的问题。
  
  #工具输出：输出格式如下
  ------------------------
  提出的问题是:xxx

  这个问题检索到的答案相关内容是:
  knowledgeTitle: xxx
  knowledgeContent: xxx
  ------------------------
  其中检索答案包含knowledgeTitle和knowledgeContent，分别代表检索的知识标题和内容，最终回答一般取knowledgeContent即可。

  #工具输入输出示例：
    工具输入: 
    宠物医保投保对宠物年龄的要求是多少？
    
    工具输出: 
    提出的问题是:宠物医保投保对宠物年龄的要求是多少？
  
    这个问题检索到的答案相关内容是:
  
    knowledgeTitle: 多大年龄可以投保
    knowledgeContent: <p>宠物医保这款产品的投、被保险人为具备完全民事行为的个人，且须为同一人，本产品仅限宠物主本人购买，其承保的宠物须为被保险人以玩赏、陪伴为目的而合法饲养的、可明确鉴别身份的年龄为60天-10周岁的犬类或猫类宠物。</p>

tool_type: 'api'
input_keys: ['input']
metadata:
  type: 'TOOL'
  module: 'sample_standard_app.intelligence.agentic.tool.pet_ins.pet_insurance_search_context_tool'
  class: 'SearchContextTool'
```

**代码实现参考**

```text
class SearchContextTool(Tool):

    def execute(self, tool_input: ToolInput):
        question = tool_input.get_data('input')
        try:
            headers = {
                "Content-Type": "application/json",
            }
            # 要发送的数据
            data = {
                "sceneCode": "ant_fortune_insurance_property",
                "query": question,
                "decoderType": "ins_slot_v2",
                "inputMethod": "user_input",
                "userInfoMap": {
                    "consultantSceneCode": "ant_fortune_insurance_property",
                },
                "enterScene": {
                    "sceneCode": "ant_fortune_insurance_property",
                }
            }
            top_k = tool_input.get_data('top_k') if tool_input.get_data('top_k') else 2
            LOGGER.info(f"search context tool input: {data}")
            response = requests.post(PRE_API_URL, headers=headers, data=json.dumps(data, ensure_ascii=False))
            result = response.json()['result']
            recallResultTuples = result.get('recallResultTuples')

            context = f"提出的问题是:{question}\n\n这个问题检索到的答案相关内容是:\n\n"
            index = 0
            for recallResult in recallResultTuples:
                if index == top_k:
                    return context
                if recallResult.get('content'):
                    context += (f"knowledgeTitle: {recallResult.get('knowledgeTitle')}\n"
                                f"knowledgeContent: {recallResult.get('content')}\n\n")
                    index += 1
            return context
        except Exception as e:
            LOGGER.error(f"invoke search context tool failed: {str(e)}")
            raise e
```

