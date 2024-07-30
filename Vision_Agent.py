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
