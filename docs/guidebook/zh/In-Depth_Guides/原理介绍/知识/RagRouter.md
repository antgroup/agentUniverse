# RagRouter

RagRouter负责将原始Query路由至不同的Store，避免在和原始问题无关的数据库中进行查询召回干扰信息，同时也可以节约计算资源。

RagRouter定义如下：
```python
from typing import List, Optional, Tuple

from agentuniverse.agent.action.knowledge.store.query import Query
from agentuniverse.base.component.component_base import ComponentEnum
from agentuniverse.base.component.component_base import ComponentBase


class RagRouter(ComponentBase):

    component_type: ComponentEnum = ComponentEnum.RAG_ROUTER
    name: Optional[str] = None
    description: Optional[str] = None

    def rag_route(self, query: Query, store_list: List[str]) \
            -> List[Tuple[Query, str]]:
        return self._rag_route(query, store_list)

    def _rag_route(self, query: Query, store_list: List[str]) \
            -> List[Tuple[Query, str]]:
        pass
```
用户在自定义的RagRouter子类中，需要重写`_rag_route`函数，其中入参为Query和一个string list，每一个string均为一个Store组件的名称，出参是一个[Query, str]的list，list中的每个元素对应一个query在某一个store上的查询任务。

在编写完对应代码后，可以参考下面的yaml将QueryParaphraser注册为aU组件：
```yaml
name: 'base_router'
description: 'base rag router map query to all store'
metadata:
  type: 'RAG_ROUTER'
  module: 'agentuniverse.agent.action.knowledge.rag_router.base_router'
  class: 'BaseRouter'
```
其中metadata的type必须为RAG_ROUTER。

### 关注您定义的RagRouter所在的包路径
在agentUniverse项目的config.toml中需要配置RagRouter配置对应的package, 请再次确认您创建的文件所在的包路径是否在`CORE_PACKAGE`中`rag_router`路径或其子路径下。

以示例工程中的配置为例，如下：
```yaml
[CORE_PACKAGE]
rag_router = ['sample_standard_app.intelligence.agentic.knowledge.rag_router']
```


## agentUniverse目前内置有以下RagRouter:
### [base_router](../../../../../../agentuniverse/agent/action/knowledge/rag_router/base_router.yaml)
该组件的的主要功能是将查询传递给系统中的所有存储库，以确保查询能够在所有可能的资源中找到答案，它也是Knowledge中默认的RagRouter。
```yaml
name: 'base_router'
description: 'base rag router map query to all store'
metadata:
  type: 'RAG_ROUTER'
  module: 'agentuniverse.agent.action.knowledge.rag_router.base_router'
  class: 'BaseRouter'
```

### [nlu_rag_router](../../../../../../agentuniverse/agent/action/knowledge/rag_router/nlu_rag_router.py)
该组件的通过配置的llm分析所有store的描述信息与原始查询文本的关联程度，从所有Store中选出最相关的N个进行查询。

该组件需要用户自己编写yaml文件，格式可参考如下：
```yaml
name: 'nlu_rag_router'
description: 'base rag router map query to all store'
store_amount: 2
llm:
  name: demo_llm
  model_name: gpt-4o
metadata:
  type: 'RAG_ROUTER'
  module: 'agentuniverse.agent.action.knowledge.rag_router.nlu_rag_router'
  class: 'NluRagRouter'
```
其中需要用户填写的内容包括：
- store_amount: 指定查询会被路由到的存储库数量，控制查询的分发范围。
- llm: 包含大语言模型的配置，用于根据Store的描述信息和Query中的query_str筛选相关的数据库。name 表示模型组件的名称，model_name 指定使用的具体模型。