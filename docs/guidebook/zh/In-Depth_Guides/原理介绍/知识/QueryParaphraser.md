# QueryParaphraser

QueryParaphraser负责对原始的Query进行加工处理，包括改写、拆分、提取关键词等，使得Query在Store中能召回更丰富且精准的内容。QueryParaphraser的输入和输出均为Query，因此query能经过多个QueryParaphraser叠加处理。

Query定义如下：
```python
from PIL.Image import Image
from typing import Optional, List, Set

from pydantic import BaseModel, Field


class Query(BaseModel):
    query_str: Optional[str] = None
    query_text_bundles: Optional[List[str]] = Field(default_factory=list)
    query_image_bundles: Optional[List[Image]] = Field(default_factory=list)
    keywords: Optional[Set[str]] = Field(default_factory=set)
    embeddings: List[List[float]] = Field(default_factory=list)
    ext_info: dict = {}
    similarity_top_k: Optional[int] = None
```
- query_str: 一个可选的字符串字段，用于存储原始查询的文本内容。
- query_text_bundles: 一个可选的字符串列表字段，用于存储多个改写后的查询文本片段。
- query_image_bundles: 一个可选的图像列表字段，用于存储多个查询图像。
- keywords: 一个可选的集合字段，用于存储查询的关键词。
- embeddings: 一个嵌入向量列表字段，用于存储查询的嵌入表示，用于相似度匹配。
- ext_info: 一个字典字段，用于存储与查询相关的额外信息，支持任意扩展。
- similarity_top_k: 一个可选的整数字段，用于指定相似度搜索中返回的最相似结果的数量。

QueryParaphraser定义如下：
```python
from abc import abstractmethod
from typing import Optional

from agentuniverse.agent.action.knowledge.store.query import Query
from agentuniverse.base.component.component_base import ComponentEnum
from agentuniverse.base.component.component_base import ComponentBase


class QueryParaphraser(ComponentBase):

    component_type: ComponentEnum = ComponentEnum.QUERY_PARAPHRASER
    name: Optional[str] = None
    description: Optional[str] = None

    @abstractmethod
    def query_paraphrase(self, origin_query: Query) -> Query:
        """Paraphrase the origin query string to different style."""
```
用户在自定义的QueryParaphraser子类中，需要重写`query_paraphrase`函数，函数的出入参均为Query形式。

在编写完对应代码后，可以参考下面的yaml将QueryParaphraser注册为aU组件：
```yaml
name: 'query_keyword_extractor'
description: 'extract keywords from query origin str'
metadata:
  type: 'QUERY_PARAPHRASER'
  module: 'agentuniverse.agent.action.knowledge.query_paraphraser.query_keyword_extractor'
  class: 'QueryKeywordExtractor'
```
其中metadata的type必须为QUERY_PARAPHRASER。
### 关注您定义的QueryParaphraser所在的包路径
在agentUniverse项目的config.toml中需要配置QueryParaphraser配置对应的package, 请再次确认您创建的文件所在的包路径是否在`CORE_PACKAGE`中`query_paraphraser`路径或其子路径下。

以示例工程中的配置为例，如下：
```yaml
[CORE_PACKAGE]
query_paraphraser = ['sample_standard_app.intelligence.agentic.knowledge.query_paraphraser']
```

## agentUniverse目前内置有以下QueryParaphraser:
### [query_keyword_extractor](../../../../../../agentuniverse/agent/action/knowledge/query_paraphraser/query_keyword_extractor.yaml)
该组件会根据Query中的原始文本提取关键词，并保存至Query的keywords字段
组件定义文件如下：
```yaml
name: 'query_keyword_extractor'
description: 'extract keywords from query origin str'
metadata:
  type: 'QUERY_PARAPHRASER'
  module: 'agentuniverse.agent.action.knowledge.query_paraphraser.query_keyword_extractor'
  class: 'QueryKeywordExtractor'
```