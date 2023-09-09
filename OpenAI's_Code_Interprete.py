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


# Save and Restore Chats:

# interpreter.chat() returns a List of messages when return_messages=True,
# which can be used to resume a conversation with interpreter.load(messages):
# messages = interpreter.chat("My name is Killian.", return_messages=True) # Save messages to 'messages'

interpreter.reset() # Reset interpreter ("Killian" will be forgotten)

interpreter.load(messages) # Resume chat from 'messages' ("Killian" will be remembered)
