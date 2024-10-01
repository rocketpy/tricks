# Composio is the best toolset to integrate AI Agents to best Agentic Tools and use them to accomplish tasks.


# https://github.com/ComposioHQ/composio

# Installation
# pip install composio-core


# Testing Composio in Action

from openai import OpenAI
from composio_openai import ComposioToolSet, App, Action


openai_client = OpenAI(api_key="{{OPENAIKEY}}")

# Initialise the Composio Tool Set
composio_tool_set = ComposioToolSet()

# Get GitHub tools that are pre-configured
actions = composio_tool_set.get_actions(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)
