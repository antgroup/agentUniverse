# Financial Event Analysis
## Case Description
This case study is based on PeerAgentTemplate & PeerWorkPattern and presents a multi-agent collaborative example focused on analyzing financial events. Specifically, regarding the topic of "Buffett's 2023 Reduction in BYD Shares"， it demonstrates how to utilize the PEER multi-agent collaboration model within the agentUniverse framework. Additionally, it provides detailed configurations and output examples for each agent in PEER.
In this case study, we utilizes the GPT-4o model by OPENAI. Prior to its usage, you need to configure the `OPENAI_API_KEY` in your environment variables.

## Agents
### Planning Agent 
Reference the original code files:
- [Configuration file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_planning_agent.yaml)
- [Prompt file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/prompt/planning_agent_cn.yaml)  

The Planning Agent is tasked with breaking down the initial  financial problem into multiple sub-problems that can be independently solved and then provided to the subsequent Executing Agent. In this particular scenario, the overarching question "Analyze the reasons for Buffett's reduction in BYD shares" can be dissected into several sub-questions, as illustrated in the diagram below.

![planning_result](../../_picture/6_4_1_planning_result.png)


### Executing Agent 
Reference the original code files:
- [Configuration file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_executing_agent.yaml)
- [Prompt file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/prompt/executing_agent_cn.yaml)

In this Agent, we provide a tool named[google_search_tool](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/tool/google_search_tool.py) for searching information on Google. To utilize this tool, you should configure `SERPER_API_KEY` in your environment variables.

The Executing Agent is responsible for solving the sub-problems that have been broken down by the Planning Agent. In this particular case, the execution results of the Executing Agent are as follows: 
![executing_result](../../_picture/6_4_1_executing_result.png)

### Expressing Agent 
Reference the original code files:
- [Configuration file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_expressing_agent.yaml)
- [Prompt file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/prompt/expressing_agent_cn.yaml)  

The Expressing Agent is responsible for summarizing all the results outputted by the Executing Agent and formulating them into an answer to the original question, adhering to the requirements specified in the prompt file. In thisinstance, the output result of the Expressing Agent is as follows:

![expressing_result](../../_picture/6_4_1_expressing_result.png)

### Reviewing Agent 
Reference the original code files:
- [Configuration file](../../../../examples/sample_apps/peer_agent_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_reviewing_agent.yaml)

The Reviewing Agent is responsible for evaluating whether the answer produced by the Expressing Agent effectively addresses the original question. In this particular case, the Reviewing Agent accepted the answer provided by the Expressing Agent:

![reviewing_result](../../_picture/6_4_1_reviewing_result.png)

### PEER Agent 
```yaml
info:
  name: 'demo_peer_agent'
  description: 'demo peer agent'
profile:
  planning: 'demo_planning_agent'
  executing: 'demo_executing_agent'
  expressing: 'demo_expressing_agent'
  reviewing: 'demo_reviewing_agent'
memory:
  name: 'demo_memory'
metadata:
  type: 'AGENT'
  module: 'agentuniverse.agent.template.peer_agent_template'
  class: 'PeerAgentTemplate'
```
Users can configure the four Agents mentioned above into a complete PEER Agent within the agentuniverse through the `PeerAgentTemplate` collaboration model. The configurations include:
- planning：The Agent responsible for the Plan part.
- executing：The Agent responsible for the Execute part.
- expressing：The Agent responsible for the Express part.
- reviewing：The Agent responsible for the Review part.

You can run the complete case in the [example file](../../../../examples/sample_apps/peer_agent_app/intelligence/test/peer_agent.py).

