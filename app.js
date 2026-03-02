
import argparse
import uvicorn
from pathlib import Path
import re

class ProjectScanner:
    PATTERNS = [r"os\.system\(", r"subprocess\.", r"eval\(", r"exec\("]

    def scan(self, path):
        results = {}
        for file in Path(path).rglob("*.py"):
            content = file.read_text(errors="ignore")
            matches = [p for p in self.PATTERNS if re.search(p, content)]
            if matches:
                results[str(file)] = matches
        return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("path", nargs="?")
    args = parser.parse_args()

    if args.command == "scan":
        scanner = ProjectScanner()
        results = scanner.scan(args.path or ".")
        print(results if results else "No obvious risks detected.")

def run_dashboard():
    uvicorn.run("openclaw_security.dashboard.server:app", host="127.0.0.1", port=8001)
