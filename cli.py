
import json
import datetime
from pathlib import Path

class AuditLogger:
    def __init__(self, log_file="security/audit.log"):
        Path("security").mkdir(exist_ok=True)
        self.log_file = log_file

    def log(self, agent, action, decision, reason=None):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "agent": agent,
            "action": action,
            "decision": decision,
            "reason": reason
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
