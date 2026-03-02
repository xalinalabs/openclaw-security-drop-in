
import yaml
from importlib import resources
from .policy_engine import PolicyEngine
from .rate_limiter import RateLimiter
from .scanners import PromptScanner, SecretScanner
from .audit_logger import AuditLogger

class SecurityAgent:

    def __init__(self, config_path=None):
        if config_path:
            with open(config_path) as f:
                self.config = yaml.safe_load(f)
        else:
            with resources.open_text("openclaw_security", "default_config.yaml") as f:
                self.config = yaml.safe_load(f)

        self.policy_engine = PolicyEngine(self.config)
        self.rate_limiter = RateLimiter()
        self.prompt_scanner = PromptScanner()
        self.secret_scanner = SecretScanner()
        self.audit_logger = AuditLogger()
        self.mode = self.config.get("mode", "enforce")

    def validate_input(self, agent_name, user_input):
        if self.prompt_scanner.scan(user_input):
            self.audit_logger.log(agent_name, "input", "blocked", "prompt_injection")
            if self.mode == "enforce":
                raise Exception("Blocked: Prompt injection detected")

    def validate_tool_call(self, agent_name, tool_name):
        policy = self.policy_engine.get_agent_policy(agent_name)
        if not self.policy_engine.is_tool_allowed(agent_name, tool_name):
            self.audit_logger.log(agent_name, "tool_call", "blocked", "tool_not_allowed")
            if self.mode == "enforce":
                raise Exception("Blocked: Tool not allowed")

        if not self.rate_limiter.allow(agent_name, policy["max_calls_per_minute"]):
            self.audit_logger.log(agent_name, "tool_call", "blocked", "rate_limit")
            if self.mode == "enforce":
                raise Exception("Blocked: Rate limit exceeded")

    def sanitize_output(self, agent_name, output):
        if self.secret_scanner.contains_secret(output):
            self.audit_logger.log(agent_name, "output", "blocked", "secret_detected")
            if self.mode == "enforce":
                return "[REDACTED]"
        return output
