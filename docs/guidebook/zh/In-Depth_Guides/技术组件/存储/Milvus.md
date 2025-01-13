## Milvus
如果您想在aU中使用Milvus 向量数据库的话您需要：

1. 安装Milvus向量数据库  
您可以参考[Milvus官方安装文档](https://milvus.io/docs/install_standalone-docker.md)安装并使用Milvus。我们推荐在Docker中启动Milvus容器的方式：
```shell
# Download the installation script
$ curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh

# Start the Docker container
$ bash standalone_embed.sh start
```
这两行命令会拉取Milvus的镜像并启动一个容器，在19530端口上提供数据库服务。
更多详细内容及其它安装方式请参考官方文档。

2. 安装milvus的python sdk
```shell
pip install pymilvus
````

### 如何配置Milvus组件
```yaml
name: 'milvus_store'
description: 'a store based on milvus'
connection_args:
  host: '127.0.0.1'
  port: '19530'
search_args:
  metric_type: "L2"
  params:
    nprobe: 10
index_params:
  metric_type: "L2"
  index_type: "HNSW"
  params:
    M: 8
    efConstruction: 32
embedding_model: 'dashscope_embedding'
similarity_top_k: 100
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.milvus_store'
  class: 'MilvusStore'
```
- connection_args: 连接 Milvus 数据库的参数，包括主机地址 (host) 和端口号 (port)。
- search_args: 搜索参数，定义了搜索时使用的距离度量类型 (metric_type) 和相关参数（如 nprobe）。
- index_params: 索引参数，定义了使用的索引类型 (index_type)、距离度量类型 (metric_type) 以及构建索引时的具体参数（如 M 和 efConstruction）。
- embedding_model: 用于生成嵌入向量的模型名称，这里指定为 dashscope_embedding。
- similarity_top_k: 在相似度搜索中返回最相似结果的数量。

### 使用方式
[知识定义与使用](../../原理介绍/知识/知识定义与使用.md)

