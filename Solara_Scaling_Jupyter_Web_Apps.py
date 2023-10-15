# Solara - Pure Python, React-style Framework for Scaling Your Jupyter and Web Apps

# https://github.com/widgetti/solara
# https://solara.dev/docs/installing
# https://solara.dev/docs/quickstart

# pip install solara

# First script
# Put the following Python snippet in a file (we suggest sol.py), or put it in a Jupyter notebook cell:

import solara

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)

@solara.component
def Page():
    # Calculate word_count within the component to ensure re-execution when reactive variables change.
    word_count = len(sentence.value.split())

    solara.SliderInt("Word limit", value=word_limit, min=2, max=20)
    solara.InputText(label="Your sentence", value=sentence, continuous_update=True)

    # Display messages based on the current word count and word limit.
    if word_count >= int(word_limit.value):
        solara.Error(f"With {word_count} words, you passed the word limit of {word_limit.value}.")
    elif word_count >= int(0.8 * word_limit.value):
        solara.Warning(f"With {word_count} words, you are close to the word limit of {word_limit.value}.")
    else:
        solara.Success("Great short writing!")


# The following line is required only when running the code in a Jupyter notebook:
Page()


# Run from the command line in the same directory where you put your file (sol.py):
# $ solara run sol.py
# Solara server is starting at http://localhost:8765

# To start a notebook server:
# $ jupyter notebook

# Jupyter lab:
# $ jupyter lab

from sol import Page
display(Page())


# Tutorial: Web app createing
"""
Generate a script file
# run the command
$ solara create button
Wrote:  /Users/maartenbreddels/github/widgetti/solara/sol.py
Run as:
$ solara run /Users/maartenbreddels/github/widgetti/solara/sol.py
"""
# This will create the sol.py file with the following content. 
import solara

clicks = solara.reactive(0)

@solara.component
def Page():
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        clicks.value += 1
        print("clicks", clicks)

    solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)
