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


# Customize System Message
# Inspect and configure Open Interpreter's system message to extend its functionality, modify permissions, or give it more context.

# interpreter.system_message +=
"""
Run shell commands with -y so the user doesn't have to confirm them.
"""
# print(interpreter.system_message)


# Change the Model
# For gpt-3.5-turbo, use fast mode:
interpreter --fast

# In Python, you will need to set the model manually:
interpreter.model = "gpt-3.5-turbo"
