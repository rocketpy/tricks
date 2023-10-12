# Solara - Pure Python, React-style Framework for Scaling Your Jupyter and Web Apps

# https://github.com/widgetti/solara
# https://solara.dev/docs/installing
# pip install solara

# First script
# Put the following Python snippet in a file (we suggest sol.py), or put it in a Jupyter notebook cell:

import solara

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)
