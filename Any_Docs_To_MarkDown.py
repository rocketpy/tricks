# MarkItDown - MarkItDown now offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop.


# https://github.com/microsoft/markitdown


# Installation
"""
To install MarkItDown, use pip: pip install 'markitdown[all]'. Alternatively, you can install it from the source:

git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e packages/markitdown[all]


# Usage

Command-Line
markitdown path-to-file.pdf > document.md
Or use -o to specify the output file:

markitdown path-to-file.pdf -o document.md
You can also pipe content:

cat path-to-file.pdf | markitdown
"""
