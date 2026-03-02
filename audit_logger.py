
class PolicyEngine:
    def __init__(self, config):
        self.config = config

    def get_agent_policy(self, agent_name):
        return self.config["agents"].get(agent_name, self.config["agents"]["default"])

    def is_tool_allowed(self, agent_name, tool_name):
        return tool_name in self.get_agent_policy(agent_name)["allowed_tools"]
