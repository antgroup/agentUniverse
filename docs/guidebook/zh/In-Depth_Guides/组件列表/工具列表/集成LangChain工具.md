# 集成LangChain工具

根据langchain中工具对象的初始化的难易程度，可以将其分为两类：
第一类，简单初始化，只需要简单的参数配置即可完成初始化。
第二类，复杂初始化，内部包含一些复杂的对象需要进行初始化。
对于一类工具，你可以在aU中直接使用配置文件进行初始化，如DuDuckGo搜索工具的初始化。
对于第二类工具，我们实现了一个LangChainTool基础类，你只需要实现该类的init_langchain_tool方法，初始化对应的langchain工具对象即可，参考维基百科的初始化方法。

注意，如果你想直接使用LangChain中的description，在配置文件中description必须要配置为空

一个工具初始化示例：
[工具地址](../../../../../../examples/sample_standard_app/intelligence/agentic/tool/samples/human_input_run.yaml)
```yaml
name: 'human_input_run'
description: ''
tool_type: 'api'
input_keys: ['input']
langchain:
  module: langchain_community.tools
  class_name: HumanInputRun
metadata:
  type: 'TOOL'
  module: 'sample_standard_app.intelligence.agentic.tool.samples.langchain_tool'
  class: 'LangChainTool'
```
参数说明：
    langchain: 你打算使用的langchain工具，需要配置module和class_name
    langchain.module: langchain的模块名，例如langchain_community.tools
    langchain.class_name: langchain的类名，例如HumanInputRun
    langchain.init_params： langchain的初始化参数，例如：
        ```yaml
        langchain:
          module: langchain_community.tools
          class_name: HumanInputRun
          init_params:
            prompt: '请输入你的问题'
        ```
    如果需要使用你完全重写了init_langchain_tool方法，那么你不需要配置该部分
该工具可以直接使用，无需任何keys

## 1. 集成LangChain中的DuckDuckGo工具
[工具地址](../../../../../../examples/sample_standard_app/intelligence/agentic/tool/samples/duckduckgo_search.yaml)
```yaml
name: 'duckduckgo_search'
description: 'DuckDuckGo Search tool'
tool_type: 'api'
input_keys: ['input']
langchain:
  module: langchain.tools
  class_name: DuckDuckGoSearchResults
  init_params:
    backend: news
metadata:
  type: 'TOOL'
  module: 'sample_standard_app.intelligence.agentic.tool.samples.langchain_tool'
  class: 'LangChainTool'
```
该工具可以直接使用，无需任何keys

## 2.集成维基百科搜索
因为LangChain的定义当中，包含一个api_wrapper对象，因此定义对象文件，并重写初始化方法：

```python
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from sample_standard_app.intelligence.agentic.tool.samples.langchain_tool import LangChainTool


class WikipediaTool(LangChainTool):
    def init_langchain_tool(self, component_configer):
        wrapper = WikipediaAPIWrapper()
        return WikipediaQueryRun(api_wrapper=wrapper)
```
定义配置
```yaml
name: 'wikipedia_query'
description: ''
tool_type: 'api'
input_keys: ['input']
metadata:
  type: 'TOOL'
  module: 'sample_standard_app.intelligence.agentic.tool.samples.wikipedia_query'
  class: 'WikipediaTool'
```