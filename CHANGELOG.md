# Changelog
**************************************
Language Version: [简体中文](CHANGELOG_zh.md) | [English](CHANGELOG.md)

This document records the version update history of the project.

## Version Number Format
The format of the version number is MAJOR.MINOR.PATCH, and the version number increment rule is as follows:
- MAJOR version when you make incompatible API changes,
- MINOR version when you add functionality in a backwards compatible manner,
- PATCH version when you make backwards compatible bug fixes.
- For more details, please refer to [Semantic Versioning 2.0.0](https://semver.org)

## Record Types
Init - Project initialization.
Added - Newly added features.
Changed - Changes to existing functionalities.
Deprecated - Soon to be deprecated features.
Removed - Features removed in this version.
Fixed - Any bug fixes.
Security - Patches and security improvements.
Note - Additional remarks regarding the version.

***************************************************

# Version Update History
# [0.0.13] - 2024-09-12
### Added
- RAG(Retrieval-Augmented Generation) Component Version Update  
This version provides a standard operating procedure for knowledge base construction and the RAG retrieval recall stage. The component covers a series of RAG atomic capabilities, including data loading, data processing, index construction, knowledge storage, intent rewriting, and retrieval re-ranking, helping users to quickly build a general RAG intelligent agent solution in open-source scenarios.

- Intelligent Agent Product Platform Update  
This version introduces new capabilities such as intelligent agent canvas orchestration, private knowledge base construction, and custom plugin support, enabling users to quickly build and orchestrate intelligent agents through a low-code, visual approach.

- Added GLM Default Model Component for Zhipu
- Added SQLiteStore Storage Component
- Added Flow Orchestration Execution Engine

### Note 
- Default path optimization for system_db_uri
The default path is already compatible with the Windows platform, for more details, please refer to [issue142](https://github.com/antgroup/agentUniverse/issues/142)
- Support for configurable chain stop words in ReactAgent
The ReactAgent YAML configuration now supports the stop_sequence keyword, allowing users to customize chain stop words. For more details, please refer to [issue127](https://github.com/antgroup/agentUniverse/issues/127)
- Added an introduction to RAG principles and a quick guide for building RAG, please pay attention to the corresponding parts in the README and user guide.
- Added advanced guidance documents for the intelligent agent productization platform, please pay attention to the corresponding parts in the README and user guide.
- Various code optimizations and documentation updates.

## [0.0.12] - 2024-08-14
### Added
- agentUniverse Product Version Offering
  - The current version provides basic capabilities for agent construction, modification, and debugging, jointly launched by the difizen project. For more details, please refer to the documentation in the product platform section.
- Monitor Component: Added knowledge and tool instance collection, supporting full-link trace sequence concatenation and providing token consumption monitoring.
- New Web Session Module: Provides session and message persistence management capabilities.

### Note
- Optimized Knowledge Component: Users can configure and specify any number of recall results (similarity_top_k).
- Fixed Chroma Component: Resolved issues where the embedding module was not specified.
- Various code optimizations and documentation updates.

## [0.0.11] - 2024-07-11
### Added
- DataAgent Autonomous Data Agent MVP Version Released
  - Minimum Viable Product version, DataAgent aims to empower your agent with the capability of self-assessment and evolution through intelligent agent abilities. For detailed information, please refer to the user documentation.
- Added intermediate information streaming output capabilities in PEER and ReAct modes

### Note
- Latest PEER research findings released
  - This paper provides a detailed introduction to the mechanisms and principles of the PEER multi-agent framework. Experimental validation proves the advancement of the PEER model. For detailed information, please refer to the user documentation.
- Added use cases
  - Andrew Ng's Reflexive Workflow Translation Agent Replication
- Some code optimizations and documentation updates.

## [0.0.10] - 2024-06-28
### Added
- Added standard integration for the DeepSeek model in the LLM module.
- Added a new OpenAI general protocol wrapper class, OpenAIStyleLLM.
  - Models using the OpenAI protocol can be configured directly.
- Added a new LangChain tool wrapper class, LangChainTool, with several example tools for search and execution.
  - LangChain tools can be configured directly.
- Added Agent information collection capability in the monitor module.

### Note
- Added use cases.
  - Supplemented documentation with a financial event analysis case study using PEER collaborative mode.
- Added several new documents for LLM components, tool components, and the Monitor module.
- Updated the new README.
- Some code optimizations and documentation updates.

## [0.0.9] - 2024-06-14
### Added
- Added standard integration for Claude and Ollama LLM components
- Added new Qwen embedding module
- Added default agents for ReAct-Type and NL2API-Type

### Note
- Added new use cases
  - RAG-Type Agent Examples: Legal Consultation Agent
  - ReAct-Type Agent Examples: Python Code Generation and Execution Agent
  - Multi-Agent: Discussion Group Based on Multi-Turn Multi-Agent Mode

  For more details, please refer to the use case section in the user documentation.
- Some code optimizations and documentation updates.

## [0.0.8] - 2024-06-06
### Added
- Introduced a new monitor module
  - Data running in any agentUniverse can be collected and observed
- Added webserver post_fork functionality
  - Provides multi-node process intervention capabilities after starting the webserver in agentUniverse
- Introduced SQLDB_WRAPPER wrapper class, offering typical database connection methods
  - Through the SQLDB_WRAPPER wrapper class, you can conveniently connect to various databases and storage technologies including SQLServer, MySQL, Oracle, PostgreSQL, SQLite and others
- Added connection support for Milvus vector database component

For more usage of the above features, please pay attention to the agentUniverse guidebook.

### Changed
- Flask is set as the default webserver startup method across all platforms, with gunicorn and gRPC capabilities disabled by default
  - In the previous version, we found slight compatibility differences with gunicorn and gRPC across different operating systems. Thus, we have made Flask the primary startup method for all platforms. You can enable gunicorn and gRPC in the configuration as needed.

### Security
- Some aU dependencies were identified to have security vulnerabilities in third-party packages. For security reasons, we have upgraded their versions, with the main changes including:
  - requests (^2.31.0 -> ^2.32.0)
  - flask (^2.2 -> ^2.3.2)
  - werkzeug (^2.2.2 -> ^3.0.3)
  - langchain (0.0.352 -> 0.1.20)
  - langchain-core (0.1.3 -> 0.1.52)
  - langchain-community (no version lock -> 0.0.38)
  - gunicorn (21.2.0 -> ^22.0.0)
  - Jinja2 (no version lock -> ^3.1.4)
  - tqdm (no version lock -> ^4.66.3)
If your system has external access, we strongly recommend installing version v0.0.8 of agentUniverse to mitigate the security risks posed by these third-party packages. For more detailed information, you can visit https://security.snyk.io.

### Note
- Some code optimizations and documentation updates.

## [0.0.7] - 2024-05-29
### Added
- LLM component supports multimodal parameter invocation.
- Added LLM integration methods for Qwen, WenXin, Kimi, Baichuan, etc.

### Note
- Added a multimodal example agent, see the invocation details in `sample_standard_app.intelligence.test.test_multimodal_agent.MultimodalAgentTest`.
- Some code optimizations and documentation updates.

## [0.0.6] - 2024-05-15
### Added
- Support for the GPT-4o model, with updates to related examples.
- Support for the RPC component gRPC, providing a standard method for service startup.

### Note 
- Provide standard Docker images and K8S deployment solutions.
- Some code optimizations and documentation updates.

## [0.0.5] - 2024-05-08
### Added
- The LLM component supports streaming calls.
- The Knowledge component adds an update definition.

### Fixed
- Fixed potential concurrency safety issues in the peer planner.
- Fixed the issue in version 0.0.4 of the PyPI package where the packaging method forced users to enter an AK upon startup.

### Note 
- Some code optimizations and documentation updates.

## [0.0.4] - 2024-04-26
### Added
- Add version management capability to the prompt.

### Fixed
- Fixed compatibility issues on Windows
  * Due to compatibility issues of Gunicorn with Windows systems, automatically identify the kernel version to select the web startup method.
  * Specified YAML reading as UTF-8 encoding method.

### Note
- [2024-05-08] Please be aware that the PyPI package version 0.0.4 includes the sample_standard_app example project by default. This will reference additional components from sample_standard_app at startup and require users to input an AK. If you are not using the corresponding components, you can bypass this restriction by using a mock AK. This issue has been fixed in version 0.0.5.

## [0.0.3] - 2024-04-19
### Init
- The official release version of AgentUniverse has been initialized. Enjoy using it!

## [0.0.2] - 2024-04-17
### Fixed
- Fixed an issue where associated dependencies were not being automatically installed when installing package versions.

## [0.0.1] - 2024-04-09
### Init
- Project initialization commit. This framework is a large model multi-agent framework. Enjoy using it!