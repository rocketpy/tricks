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
