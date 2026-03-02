
from openclaw_security import SecurityAgent
from openclaw_security.middleware import SecurityMiddleware

security = SecurityAgent()
middleware = SecurityMiddleware(security)

def agent_run(input_data):
    return "Agent output"

secure_run = middleware.wrap_agent("default", agent_run)

print(secure_run("test input"))
