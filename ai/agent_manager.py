# jarvis/ai/agent_manager.py
# Multi-agent coordination
class AgentManager:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name, agent):
        self.agents[agent_name] = agent

    def get_agent(self, agent_name):
        return self.agents.get(agent_name)
