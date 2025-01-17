# Integrated LangChain Tool

Based on the level of difficulty in initializing tool objects in LangChain, they can be divided into two categories:
The first category involves simple initialization, where initialization can be completed with basic parameter configuration.
The second category involves complex initialization with intricate internal objects that need to be set up.
For the first category of tools, you can use configuration files in aU to directly perform initialization, such as initializing the DuDuckGo search tool.
For the second category of tools, we have implemented a LangChainTool base class. You only need to implement the init_langchain_tool method of this class to initialize the corresponding LangChain tool objects, with reference to the initialization method of Wikipedia.

Note: If you want to directly use the description from LangChain, the description in the configuration file must be set to empty.

An Example of Tool Initialization:
[Tool Path](../../../../../../examples/sample_standard_app/intelligence/agentic/tool/samples/human_input_run.yaml)
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
Parameter Description:
    langchain: The LangChain tool you intend to use, which requires the configuration of module and class_name.
    langchain.module: The name of the LangChain module, e.g., langchain_community.tools.
    langchain.class_name: The name of the LangChain class, e.g., HumanInputRun.
    langchain.init_params: The initialization parameters for LangChain, such as:
        ```yaml
        langchain:
          module: langchain_community.tools
          class_name: HumanInputRun
          init_params:
            prompt: 'please Input your question'
        ```
    If you completely override the `init_langchain_tool` method, then you do not need to configure this part.

## 1. Integrate the DuckDuckGo Tool from LangChain
[Tool Path](../../../../../../examples/sample_standard_app/intelligence/agentic/tool/samples/duckduckgo_search.yaml)
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
This tool can be used directly without any keys.

## 2.Integrate Wikipedia Search
Since the definition of LangChain includes an api_wrapper object, define the object file and override the initialization method:

```python
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from sample_standard_app.intelligence.agentic.tool.samples.langchain_tool import LangChainTool


class WikipediaTool(LangChainTool):
    def init_langchain_tool(self, component_configer):
        wrapper = WikipediaAPIWrapper()
        return WikipediaQueryRun(api_wrapper=wrapper)
```
Define Configuration:
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