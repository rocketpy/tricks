# MoneyPrinter - Automate the creation of YouTube Shorts locally, simply by providing a video topic to talk about.

# https://github.com/FujiwaraChoki/MoneyPrinter

# Installation
"""
git clone https://github.com/FujiwaraChoki/MoneyPrinter.git
cd MoneyPrinter

# Install requirements
pip install -r requirements.txt

# Copy .env.example and fill out values
cp .env.example .env

# Run the backend server
cd Backend
python main.py

# Run the frontend server
cd ../Frontend
python -m http.server 3000
"""

# Usage
"""
Copy the .env.example file to .env and fill in the required values
Open http://localhost:3000 in your browser
Enter a topic to talk about
Click on the "Generate" button
Wait for the video to be generated
The video's location is temp/output.mp4
Fonts
Add your fonts to the fonts/ folder, and load them by specifying the font name on line 124 in Backend/video.py.
"""
