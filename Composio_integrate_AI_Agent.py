# Composio is the best toolset to integrate AI Agents to best Agentic Tools and use them to accomplish tasks.


# https://github.com/ComposioHQ/composio

# https://docs.composio.dev/introduction/intro/overview

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

my_task = "Star a repo composiodev/composio on GitHub"

# Setup openai assistant
assistant_instruction = "You are a super intelligent personal assistant"

assistant = openai_client.beta.assistants.create(
    name="Personal Assistant",
    instructions=assistant_instruction,
    model="gpt-4-turbo",
    tools=actions,
)

# create a thread
thread = openai_client.beta.threads.create()

message = openai_client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=my_task
)

# Execute Agent with integrations
run = openai_client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)


# Execute Function calls
response_after_tool_calls = composio_tool_set.wait_and_handle_assistant_tool_calls(
    client=openai_client,
    run=run,
    thread=thread,
)

# print(response_after_tool_calls)


# Examples

# Imports and Environment Setup
import os
import dotenv
from textwrap import dedent
from composio_langchain import Action, App, ComposioToolSet
from langchain_openai import ChatOpenAI
from composio.local_tools import ragtool


# Load environment variables
dotenv.load_dotenv()

# Initialize Language Model and Define Tools

# Initialize the LLM with the OpenAI GPT-4o model and API key
llm = ChatOpenAI(model="gpt-4o")

# Initialize the Composio ToolSet
toolset = ComposioToolSet()

# Get the RAG tool from the Composio ToolSet
tools = toolset.get_tools(apps=[App.RAGTOOL])


# Define the RAG Agent
rag_agent = Agent(
    role="RAG Agent",
    goal=dedent(
        """\
        Add relevant content to the RAG tool to enrich its knowledge base.
        Formulate a query to retrieve information from the RAG tool based on user input.
        After retrieval and addition of content, evaluate whether the goal given by the user input is achieved. If yes, stop execution."""
    ),
    verbose=True,
    memory=True,
    backstory=dedent(
        """\
        You are an expert in understanding user requirements, forming accurate queries,
        and enriching the knowledge base with relevant content."""
    ),
    llm=llm,
    allow_delegation=False,
    tools=tools,
)

# Define Tasks for Adding Content
from composio_langchain import Task  # Ensure Task is imported

# User-provided description of the data to be added
additional_content_list = [
    "Paris is the capital of France. It is known for its art, fashion, and culture.",
    "Berlin is the capital of Germany. It is famous for its history and vibrant culture.",
    "Tokyo is the capital of Japan. It is known for its technology and cuisine.",
    "Canberra is the capital of Australia. It is known for its modern architecture and museums.",
    # Add more data as needed
]

# Define the task for adding content to the RAG tool
add_content_tasks = [
    Task(
        description=dedent(
            f"""\
            Add the following content to the RAG tool to enrich its knowledge base: {content}"""
        ),
        expected_output="Content was added to the RAG tool",
        tools=tools,
        agent=rag_agent,
        allow_delegation=False,
    )
    for content in additional_content_list
]


# JS
# Install the Composio SDK:
# npm install composio-core

# Setup the OpenAI and Composio Tool Set:

# import { OpenAI } from "openai";
# import { OpenAIToolSet } from "composio-core";


# const toolset = new OpenAIToolSet({
#     apiKey: process.env.COMPOSIO_API_KEY,
# });

# async function setupUserConnectionIfNotExists(entityId) {
#     const entity = await toolset.client.getEntity(entityId);
#     const connection = await entity.getConnection('github');

#     if (!connection) {
#         // If this entity/user hasn't already connected the account
#         const connection = await entity.initiateConnection(appName);
#         console.log("Log in via: ", connection.redirectUrl);
#         return connection.waitUntilActive(60);
#     }

#     return connection;
# }
