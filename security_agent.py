
import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(deque)

    def allow(self, agent_name, limit):
        now = time.time()
        window = 60

        while self.calls[agent_name] and self.calls[agent_name][0] < now - window:
            self.calls[agent_name].popleft()

        if len(self.calls[agent_name]) >= limit:
            return False

        self.calls[agent_name].append(now)
        return True
