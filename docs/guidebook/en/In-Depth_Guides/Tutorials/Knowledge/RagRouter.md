# RagRouter

The RagRouter is responsible for routing the original Query to different Stores, preventing unnecessary queries in unrelated databases, which could otherwise introduce irrelevant information and waste computational resources.

The RagRouter is defined as follows:
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
When creating a custom subclass of RagRouter, you need to override the `_rag_route` function. This function takes a Query and a list of strings as input, where each string corresponds to the name of a Store component. The output is a list of [Query, str] tuples, where each element represents a query task for a specific store.

After writing code, you can refer to the following YAML configuration to register the RagRouter as an aU component:
```yaml
name: 'base_router'
description: 'base rag router map query to all store'
metadata:
  type: 'RAG_ROUTER'
  module: 'agentuniverse.agent.action.knowledge.rag_router.base_router'
  class: 'BaseRouter'
```
The `metadata.type` must be set to RAG_ROUTER.

### Pay Attention to the Package Path of Your Custom RagRouter:
In the config.toml file of the agentUniverse project, you need to configure the package path corresponding to your RagRouter. Please double-check whether the path of the file you created is under the rag_router path or its subdirectories in CORE_PACKAGE.

For example, the configuration in the sample project is as follows:
```yaml
[CORE_PACKAGE]
rag_router = ['sample_standard_app.intelligence.agentic.knowledge.rag_router']
```


## The following RagRouters are built into agentUniverse:
### [base_router](../../../../../../agentuniverse/agent/action/knowledge/rag_router/base_router.yaml)
This component's primary function is to route the query to all the stores in the system, ensuring that the query can find answers in all possible resources. It is also the default RagRouter in Knowledge.
```yaml
name: 'base_router'
description: 'base rag router map query to all store'
metadata:
  type: 'RAG_ROUTER'
  module: 'agentuniverse.agent.action.knowledge.rag_router.base_router'
  class: 'BaseRouter'
```

### [nlu_rag_router](../../../../../../agentuniverse/agent/action/knowledge/rag_router/nlu_rag_router.py)
This component selects the most relevant stores by analyzing the correlation between the description of all stores and the original query text using a configured language model (LLM).

Users need to create their own YAML file for this component, with a format similar to the following:
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
The fields that users need to fill out include:
- store_amount: Specifies the number of stores to which the query will be routed, controlling the distribution range of the query.
- llm: Contains the configuration of the large language model used to filter relevant databases based on the Store descriptions and the query_str in the Query. The name refers to the name of the model component, and model_name specifies the specific model used.