# OpenClaw Security

Drop-in security module for OpenClaw AI agents.

## Installation

pip install openclaw-security

## Usage

from openclaw_security import SecurityAgent

security = SecurityAgent()

security.validate_input(agent_name, user_input)
security.validate_tool_call(agent_name, tool_name)
response = security.sanitize_output(agent_name, response)

## Modes

monitor  - logs only
enforce  - blocks violations

🚀 How To Build & Install Locally

Inside project root:

pip install build
python -m build
pip install dist/openclaw_security-0.1.0-py3-none-any.whl

Or editable mode:

pip install openclaw-security

Then:

from openclaw_security import SecurityAgent
security = SecurityAgent()

That’s it.

Zero friction.

pip install openclaw-security
openclaw-sec scan .
