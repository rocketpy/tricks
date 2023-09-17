# InstaGraph - application for converting text or URLs into insightful knowledge graphs. 

# https://github.com/yoheinakajima/instagraph

# For non-coders: https://instagraph.ai/

# Installation
"""
To get started, you'll need Python and pip installed.
1. Clone the repository
git clone https://github.com/yoheinakajima/instagraph.git

2. Navigate to the project directory
cd instagraph

3. Install the required Python packages
pip install -r requirements.txt

4. Set up your OpenAI API Key
Change .env.example to .env ''' bash mv .env.example .env ''' Add your OpenAI API key to .env file:
OPENAI_API_KEY=your-api-key-here

5. Run the Flask app
python main.py
Navigate to http://localhost:8080 to see your app running.
"""

# Usage
"""
Web Interface
Open your web browser and navigate to http://localhost:8080.
Type your text or paste a URL in the input box.
Click "Submit" and wait for the magic to happen!
API Endpoints
GET Response Data: /get_response_data

Method: POST
Data Params: {"user_input": "Your text here"}
Response: GPT-3.5 processed data
GET Graph Data: /get_graph_data

Method: POST
Response: Graph Data
GET History Data: /get_graph_history

Method: GET
Response: Graph Data
"""

