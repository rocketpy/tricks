# Open Interpreter - Let language models run code on your computer.
# An open-source, locally running implementation of OpenAI's Code Interpreter.

# https://github.com/KillianLucas/open-interpreter


# pip install open-interpreter

# Terminal:
# interpreter

# Python
import interpreter

interpreter.chat("Plot APPL and META's normalized stock prices") # Executes a single command
interpreter.chat() # Starts an interactive chat


# Start a New Chat
# In Python, Open Interpreter remembers conversation history. If you want to start fresh, you can reset it:

interpreter.reset()
