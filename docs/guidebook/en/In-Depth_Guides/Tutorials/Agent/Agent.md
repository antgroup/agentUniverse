# Agent
An agent is capable of autonomously acting to achieve goals set by humans, having capabilities for learning, reasoning, decision-making, and execution. It accomplishes objectives through steps such as task decomposition, using tools and knowledge, and progress control, and then independently completes its tasks. Within agentUniverse, an agent is one of the most critical domain components. It integrates a series of other domain components, including tools, knowledge, and plans, into a cohesive and efficient system, ultimately completing the tasks assigned to it by people.
The performance of an agent directly impacts the effectiveness of application service. In complex service scenarios, often one or multiple competent agents are required to complete tasks. In agentUniverse, utilizing the achievements of industry and academia as well as practical experience in industry implementation, the following definition for agents is established, as shown in the figure.
![](../../../../_picture/agent.jpg)

Let's introduce the roles of the various components within the Agent component separately.

## Profile
This section is the global settings of the Agent, including the Agent's Target, Introduction, and LLM parts.

### Introduction
For the description of the Agent's role, such as being an AI assistant skilled in information analysis.

### Target
The goal that the Agent needs to achieve. The Agent will focus on this goal to complete a series of subsequent tasks.
  
```text
When setting the goal for an agent, it needs to be concise and impactful, describing a directional duty goal. Providing a specific and specialized domain scope is optimal.

✅ Good examples: answering questions in the finance domain, rewriting for code performance optimization.

❌ Bad examples: aimless descriptions such as "just chatting."
```
  
### Instruction
It includes specific settings for the Agent, such as personality traits, background knowledge, and behavioral patterns.

```text
How to write a good Instruction? We can adopt the following paradigm:
A clear scope of responsibilities the agent excels in (recommended) + Personality setting (fill in as needed) + 
Background knowledge (fill in as needed) + 
User input format (fill in as needed) + 
Behavioral guidance (recommended) + 
Agent output format (fill in as needed) + 
Practical examples - fewshot (recommended)

Following the above paradigm, here is an example definition:
✅ For instance, a good example would be:
You are Jerry's personal exclusive chatbot [The role played by the agent].
You excel at answering various professional questions encountered in life and casual conversations, particularly proficient at answering financial questions [A clear scope of responsibilities the agent excels in].
Your personality is cheerful and lively [Personality setting].
Jerry is especially interested in financial news on weekdays and also pays attention to macro-level policies [Background knowledge].
Jerry will communicate with you in the form of natural language for questions and answers [User input format]. 
Please adhere to the following principles in your responses: for professional-type questions, give priority to using knowledge retrieval tools for summarization and answering. Take professional questions seriously, and if you cannot arrive at a confident conclusion, please honestly communicate that to Jerry [Behavioral guidance].
Please output your response in the form of natural language [Agent output format].
Here is an actual example of communication with Jerry: Jerry asks how to view the macroeconomic data of December 2023? Response: The CPI has turned from a decrease to an increase month-on-month, with the year-on-year decline narrowing in December. Affected by factors such as cold weather and increased demand for consumption before the holiday, the CPI has turned from a decrease to an increase month-on-month, with the year-on-year decline narrowing; excluding food and energy prices, the core CPI rose by 0.6% year-on-year, with the increase remaining stable. The PPI declined month-on-month, with the year-on-year decline narrowing in December, affected by continuing decreases in international oil prices and insufficient demand for some industrial products, the national PPI declined month-on-month, with the year-on-year decline narrowing. [Practical example - fewshot]
(The text within [] symbols is for explanation, and actual submissions do not require prompts).

❌ For instance, a bad example would be:
You are skilled at providing various fitness plans tailored to different groups of people (the information provided is too scant, resulting in high uncertainty in outcomes, leading to generic advice that often does not meet the actual demands).
```

### LLM
The LLM utilized by the Agent. agentUniverse offers a wide array of existing LLM components and standard customization options for LLMs. You can choose to use or define the LLMs you need. We will detail how they work in the LLM section.

## Planning
This section will impact the collaboration and execution strategies during the actual work of the Agent. It embodies the collaborative and execution ideas of patterns. Planning will include various types, such as making the Agent follow a completely manually orchestrated workflow, adhere to a specific standard operating procedure (SOP), or use certain specific working methods like the Retrieval-Augmented Generation (RAG), or allowing the agent to work entirely autonomously (Auto). Of course, Planning can not only affect the execution strategy of a single agent but can also involve or coordinate any other agents in the plan. For example, PEER is a typical multi-agent collaboration mode, which we will focus on introducing in other sections due to its interesting collaborative method.

## Action
This section primarily consists of tools and knowledge. Just as humans use tools and knowledge to complete tasks, agents need to acquire additional knowledge and skills, as well as incorporate additional tools, during the process of performing complex tasks, which will improve their performance in specific domains. 

### Tool
Tools available to Agents. agentUniverse offers a variety of existing tool components and standard methods for customizing tools. You have the option to use or define required tools and load them into the agent through configuration settings. Utilizing the underlying technological components provided by agentUniverse, such as HTTP and GRPC capabilities, enables you to register any third-party service, existing internal corporate service, or local function as a tool. Detailed descriptions of how they operate will be provided in the Tool section.

### Knowledge
Knowledge accessible to Agents. agentUniverse offers a wide range of existing Knowledge components and standard customization methods. You can choose to use or define the Knowledge you need, and then integrate it into the Agent via configuration settings. In addition, agentUniverse supports the integration of underlying storage technology middleware, such as SQLite, Chroma, and other storage solutions, enabling you to access data from various storage options. We will explain in detail how they work in the Knowledge section.

## Memory
The memory resources available to agents. agentUniverse offers a range of standard memory options, and in most cases, users do not need to be concerned with the specific implementation of memory. The memory component also offers the capability for users to customize it. We will explain in detail how they work in the memory section.

# Conclusion
Up to this point, you have acquired a comprehensive understanding of the components and underlying principles of an agent within the agentUniverse framework. In the subsequent section, we will delve specifically into the standard definitions of agent components, the process of customizing an Agent, and the methodologies for utilizing an agent, along with other pertinent topics.