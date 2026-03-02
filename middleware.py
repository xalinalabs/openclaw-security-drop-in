
import re

class PromptScanner:
    PATTERNS = [
        r"ignore previous instructions",
        r"reveal system prompt",
        r"send me your api key",
        r"<script>"
    ]

    def scan(self, text):
        text = text.lower()
        return any(re.search(p, text) for p in self.PATTERNS)


class SecretScanner:
    PATTERNS = [
        r"sk-[A-Za-z0-9]{32,}",
        r"AKIA[0-9A-Z]{16}",
        r"Bearer\s+[A-Za-z0-9\-_.]+"
    ]

    def contains_secret(self, text):
        return any(re.search(p, text) for p in self.PATTERNS)
