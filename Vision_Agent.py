# Vision Agent - is a library that helps you utilize agent frameworks to generate code to solve your vision task.

# https://github.com/landing-ai/vision-agent


# pip install vision-agent

# Ensure you have an OpenAI API key and set it as an environment variable (if you are using Azure OpenAI please see the Azure setup section):
# export OPENAI_API_KEY="your-api-key"


# Basic Usage
# To run the streamlit app locally to chat with Vision Agent, you can run the following command:
"""
pip install -r examples/chat/requirements.txt
export WORKSPACE=/path/to/your/workspace
export ZMQ_PORT=5555
streamlit run examples/chat/app.py
"""


# Basic Programmatic Usage
rom vision_agent.agent import VisionAgent

agent = VisionAgent()
resp = agent("Hello")
# print(resp)
# [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "{'thoughts': 'The user has greeted me.
# I will respond with a greeting and ask how I can assist them.', 'response': 'Hello! How can I assist you today?', 'let_user_respond': True}"}]
resp.append({"role": "user", "content": "Can you count the number of people in this image?", "media": ["people.jpg"]})
resp = agent(resp)


# Which produces the following code:
from vision_agent.tools import load_image, grounding_sam

def calculate_filled_percentage(image_path: str) -> float:
    # Step 1: Load the image
    image = load_image(image_path)

    # Step 2: Segment the jar
    jar_segments = grounding_sam(prompt="jar", image=image)

    # Step 3: Segment the coffee beans
    coffee_beans_segments = grounding_sam(prompt="coffee beans", image=image)

    # Step 4: Calculate the area of the segmented jar
    jar_area = 0
    for segment in jar_segments:
        jar_area += segment['mask'].sum()

    # Step 5: Calculate the area of the segmented coffee beans
    coffee_beans_area = 0
    for segment in coffee_beans_segments:
        coffee_beans_area += segment['mask'].sum()

    # Step 6: Compute the percentage of the jar area that is filled with coffee beans
    if jar_area == 0:
        return 0.0  # To avoid division by zero
    filled_percentage = (coffee_beans_area / jar_area) * 100

    # Step 7: Return the computed percentage
    return filled_percentage


""""
agent = VisionAgentCoder(verbose=2)

Detailed Usage:
You can also have it return more information by calling chat_with_workflow.
The format of the input is a list of dictionaries with the keys role, content, and media:

results = agent.chat_with_workflow([{"role": "user", "content": "What percentage of the area of the jar is filled with coffee beans?", "media": ["jar.jpg"]}])
print(results)

{
    "code": "from vision_agent.tools import ..."
    "test": "calculate_filled_percentage('jar.jpg')",
    "test_result": "...",
    "plan": [{"code": "...", "test": "...", "plan": "..."}, ...],
    "working_memory": ...,
}
"""

# Multi-turn conversations
# You can have multi-turn conversations with vision-agent as well, giving it feedback on the code and having it update.
# You just need to add the code as a response from the assistant:

agent = va.agent.VisionAgent(verbosity=2)
conv = [
    {
        "role": "user",
        "content": "Are these workers wearing safety gear? Output only a True or False value.",
        "media": ["workers.png"],
    }
]
result = agent.chat_with_workflow(conv)
code = result["code"]
conv.append({"role": "assistant", "content": code})
conv.append(
    {
        "role": "user",
        "content": "Can you also return the number of workers wearing safety gear?",
    }
)
result = agent.chat_with_workflow(conv)


# Tools
# There are a variety of tools for the model or the user to use.
# Some are executed locally while others are hosted for you.
# You can also ask an LMM directly to build a tool for you. For example:

import vision_agent as va

lmm = va.lmm.OpenAILMM()
detector = lmm.generate_detector("Can you build a jar detector for me?")
detector(va.tools.load_image("jar.jpg"))
[{"labels": ["jar",],
  "scores": [0.99],
  "bboxes": [
    [0.58, 0.2, 0.72, 0.45],
  ]
}]


# add custom tools to the agent:

import vision_agent as va
import numpy as np

@va.tools.register_tool(imports=["import numpy as np"])
def custom_tool(image_path: str) -> str:
    """My custom tool documentation.

    Parameters:
        image_path (str): The path to the image.

    Returns:
        str: The result of the tool.

    Example
    -------
    >>> custom_tool("image.jpg")
    """

    return np.zeros((10, 10))
