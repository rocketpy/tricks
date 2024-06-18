# Translation Agent - Agentic translation using reflection workflow

# https://github.com/andrewyng/translation-agent


"""
# Features:
This is a Python demonstration of a reflection agentic workflow for machine translation. The main steps are:

Prompt an LLM to translate a text from source_language to target_language.
Have the LLM reflect on the translation to come up with constructive suggestions for improving it.
Use the suggestions to improve the translation.


# Examples
This directory contains example scripts demonstrating the usage of the translation-agent workflow.

# Contents
example_script.py: A simple script showing how to perform machine translation using the package.
sample-texts/: A directory containing a few sample texts from The Batch letters written by Andrew and Data Points summaries found on the DeepLearning.ai website.

# Usage
To run the example scripts, ensure that you have installed the translation-agent package and have activated your virtual environment.

# Then run:

python example_script.py
"""


# Usage
import translation_agent as ta

source_lang, target_lang, country = "English", "Spanish", "Mexico"
translation = ta.translate(source_lang, target_lang, source_text, country)


# Example script
import os
import translation_agent as ta


if __name__ == "__main__":
    source_lang, target_lang, country = "English", "Spanish", "Mexico"

    relative_path = "sample-texts/sample-short1.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    print(f"Source text:\n\n{source_text}\n------------\n")

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    print(f"Translation:\n\n{translation}")
