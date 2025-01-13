# 版本说明
**************************************
语言版本: [简体中文](CHANGELOG_zh.md) | [English](CHANGELOG.md)

本文件用于记录项目的版本更新历史。

## 版本号格式
版本号格式为 `主版本号.次版本号.修订号`，版本号递增规则如下：
- 主版本号：当你做了不兼容的 API 修改时，递增主版本号。
- 次版本号：当你做了向下兼容的功能性新增时，递增次版本号。
- 修订号：当你做了向下兼容的问题修正时，递增修订号。
- 详细说明请参考 [语义化版本 2.0.0](https://semver.org)

## 记录类型
Init - 项目初始化。
Added - 新增的功能。
Changed - 对现有功能的更改。
Deprecated - 即将废弃的功能。
Removed - 现版本中移除的功能。
Fixed - 任何错误修复。
Security - 补丁与安全改进。
Note - 对于版本的额外说明。

***************************************************

# 版本更新记录
## [0.0.13] - 2024-09-12
### Added
- RAG检索增强能力组件版本更新  
本版本提供知识库构建、RAG检索召回环节标准作业流程，组件覆盖数据加载、数据处理、索引构建、知识入库、意图改写、检索重排等一系列RAG原子能力，帮助用户在开源场景下快速构建通用RAG智能体方案。

- 智能体产品化平台更新  
本版本新增支持智能体画布编排、私有知识库构建、自定义插件等能力，通过低代码、可视化的方式帮助用户快速构建与编排智能体。

- 新增智谱GLM默认模型组件
- 新增SQLiteStore存储组件
- 新增flow编排执行引擎

### Note 
- system_db_uri默认路径优化  
默认路径已兼容windows平台，详情见[issue142](https://github.com/antgroup/agentUniverse/issues/142)
- ReactAgent支持链停止词配置化  
ReactAgent yaml配置目前已经支持stop_sequence关键词，用户可以自行配置链停止词,详情见[issue127](https://github.com/antgroup/agentUniverse/issues/127)
- 新增RAG原理介绍与RAG快速构建指导文档，请关注README与用户指南相应部分。
- 新增智能体产品化平台高阶指导文档，请关注README与用户指南相应部分。
- 部分代码优化与文档更新

## [0.0.12] - 2024-08-14
### Added
- agentUniverse产品化版本提供
  - 当前版本提供智能体构建、修改、调试等基础能力，由difizen项目联合推出，更多详情请见文档产品化平台部分。
- monitor组件新增对于知识、工具实例采集，支持全链路trace时序串联并提供token消耗监控
- 新增web会话模块，提供session与message持久化管理能力

### Note
- 优化知识组件，可由用户配置指定任意召回结果数量（similarity_top_k）
- 修复chroma组件未指定embedding模块出现异常
- 其他部分代码优化与文档更新

## [0.0.11] - 2024-07-11
### Added
- DataAgent数据自治智能体MVP版本发布
  - Minimum Viable Product版本，DataAgent旨在使用智能体能力让您的Agent拥有自我评价与演进的能力，详细内容请查阅用户文档。
- 增加PEER、ReAct模式中间信息流式输出能力

### Note
- PEER最新研究成果发布
  - 该文献详细介绍了PEER多智能体框架的机制原理，同时在实验部分通过验证证明了PEER模式的先进性，详细内容请查阅用户文档。
- 新增使用案例
  - 吴恩达反思工作流翻译智能体复刻
- 部分代码优化与文档更新

## [0.0.10] - 2024-06-28
### Added
- LLM组件新增DeepSeek模型标准接入
- 新增OpenAI通用协议包装类OpenAIStyleLLM
  - openai协议类模型接入可直接配置
- 新增LangChain工具包装类LangChainTool，新增搜索类、执行类示例工具若干
  - LangChain工具接入可直接配置
- monitor模块新增Agent纬度信息采集能力

### Note
- 新增使用案例
  - PEER协同模式的金融事件分析案例文档补充
- 新增若干LLM组件、工具组件、Monitor模块文档
- 新版README更新
- 部分代码优化与文档更新

## [0.0.9] - 2024-06-14
### Added
- LLM组件新增claude、ollama标准接入
- 新增qwen embedding模块
- 新增ReAct、nl2api默认agent

### Note
- 新增使用案例
  - RAG类Agent案例-法律咨询Agent
  - ReAct类Agent案例-Python代码生成与执行Agent
  - 多智能体案例-基于多轮多Agent的讨论小组

  详情请看用户文档案例部分。
- 部分代码优化与文档更新

## [0.0.8] - 2024-06-06
### Added
- 新增monitor模块
  - 任何agentUniverse运行时的数据可以被采集与观测
- 新增webserver post_fork功能
  - 开放agentUniverse中webserver启动后的多节点流程干预功能
- 新增SQLDB_WRAPPER包装类，提供典型数据库连接方式
  - 通过SQLDB_WRAPPER包装类您可以非常方便的连接如SQLServer、MySQL、Oracle、PostgreSQL、SQLite等几十种数据库与存储技术组件。
- 新增milvus向量数据库组件连接

上述功能更多用法请关注agentUniverse指导手册部分。

### Changed
- 全平台以flask作为默认webserver启动方式，gunicorn与GRPC能力置为默认关闭
  - 我们在上个版本中发现不同的操作系统对于gunicorn与GRPC的兼容性会有略微差异，我们将flask作为全平台的第一启动方式，您可以按需在配置中开启gunicorn与GRPC。

### Security
- 部分aU依赖第三方包识别到安全漏洞，出于安全考虑我们对其进行版本升级，主要包含如下变动：
  - requests (^2.31.0 -> ^2.32.0)
  - flask (^2.2 -> ^2.3.2)
  - werkzeug (^2.2.2 -> ^3.0.3)
  - langchain (0.0.352 -> 0.1.20)
  - langchain-core (0.1.3 -> 0.1.52)
  - langchain-community (no version lock -> 0.0.38)
  - gunicorn (21.2.0 -> ^22.0.0)
  - Jinja2 (no version lock -> ^3.1.4)
  - tqdm (no version lock -> ^4.66.3)
若您的系统存在外部访问，强烈建议您安装v0.0.8版本的aU以规避这些三方包的安全风险，更详细的说明您可以关注https://security.snyk.io。

### Note
- 部分代码优化与文档更新

## [0.0.7] - 2024-05-29
### Added
- LLM组件支持多模态参数调用
- 新增通义千问、文心一言、Kimi、百川等常用LLM接入方式

### Note 
- 添加多模态样例agent调用详情见`sample_standard_app.intelligence.test.test_multimodal_agent.MultimodalAgentTest`
- 部分代码优化与文档更新

## [0.0.6] - 2024-05-15
### Added
- 支持gpt-4o模型, 并更新相关样例
- 支持RPC组件gGpc，并提供标准服务启动方法

### Note 
- 提供标准的aU Docker镜像与K8S部署方案，详情见指导手册
- 部分代码优化与文档更新

## [0.0.5] - 2024-05-08
### Added
- LLM组件支持流式调用
- 知识组件添加update定义

### Fixed
- 修复peer planner中可能存在的并发安全性隐患
- 修复0.0.4版本中pypi package打包方式导致启动强制要求用户填写AK问题

### Note 
- 追加部分代码优化与文档更新

## [0.0.4] - 2024-04-26
### Added
- 新增prompt版本管理能力

### Fixed
- Windows版本下的兼容问题修复
  * 由于Gunicore对于windows系统的兼容问题，自动识别内核版本自动选择web启动方式
  * yaml读取指定为utf-8 encode方式
### Note 
- [2024-05-08] 注意，0.0.4的pypi package版本中默认包含了sample_standard_app示例工程, 这将会在启动时引用sample_standard_app中的额外组件,并要求用户填写AK, 若您没有使用对应组件可以通过mock ak跳过这一限制, 这已经在0.0.5版本中修复。

## [0.0.3] - 2024-04-19
### Init
- agentUniverse正式外发版本初始化,祝您使用愉快！

## [0.0.2] - 2024-04-17
### Fixed
- 修复安装包版本时无法自动安装关联依赖包问题。 

## [0.0.1] - 2024-04-09
### Init
- 项目初始化提交,本框架是一个大模型多智能体框架,祝您使用愉快！