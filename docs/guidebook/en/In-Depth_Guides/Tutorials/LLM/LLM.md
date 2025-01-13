# LLM
LLM - Large Language Model. LLMs possess formidable capabilities for text generation and comprehension; they can understand natural language and communicate with humans using it. They are the most critical modules for agents to have learning, reasoning, decision-making, and execution capabilities, often likened to the brain of the agent. They are the intellectual core of the agent.

Currently, well-known companies such as OpenAI, Google, Anthropic, Meta, Alibaba, and Baidu all offer their own large model services. At the same time, individuals or businesses can also customize their own various LLMs using public model training and fine-tuning schemes. On model sharing platforms like HuggingFace, you can find a vast array of LLMs.

The LLM model component of agentUniverse can help you quickly access various common LLM services on the market through simple configuration. Meanwhile, the standard LLM model definition also supports your customization to access any public model service, private model service, or locally deployed model.

Different LLMs possess varying capabilities; some excel in certain evaluative dimensions, some are suited for specialized domain tasks, and others can handle multimodal tasks such as images and audio. These introduced LLM capabilities can serve as core components of an Agent, and they can also be used in any other components, such as tools. This means that you can integrate the most suitable model for your agent's use and, during multi-agent collaboration, different agents can employ different models.

# Conclusion
At this point, you have a basic understanding of the design principles of the LLM component. In the next section, we will specifically introduce you to the standard definition of the LLM component, how to custom integrate an LLM, and how to use the LLM component, etc.