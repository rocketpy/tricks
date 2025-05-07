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


# Optional Dependencies
MarkItDown has optional dependencies for activating various file formats. 
Earlier in this document, we installed all optional dependencies with the [all] option. 
However, you can also install them individually for more control. For example:

pip install 'markitdown[pdf, docx, pptx]'
will install only the dependencies for PDF, DOCX, and PPTX files.

At the moment, the following optional dependencies are available:

[all] Installs all optional dependencies
[pptx] Installs dependencies for PowerPoint files
[docx] Installs dependencies for Word files
[xlsx] Installs dependencies for Excel files
[xls] Installs dependencies for older Excel files
[pdf] Installs dependencies for PDF files
[outlook] Installs dependencies for Outlook messages
[az-doc-intel] Installs dependencies for Azure Document Intelligence
[audio-transcription] Installs dependencies for audio transcription of wav and mp3 files
[youtube-transcription] Installs dependencies for fetching YouTube video transcription


# Plugins
MarkItDown also supports 3rd-party plugins. Plugins are disabled by default. To list installed plugins:

markitdown --list-plugins
To enable plugins use:

markitdown --use-plugins path-to-file.pdf
To find available plugins, search GitHub for the hashtag #markitdown-plugin. To develop a plugin, see packages/markitdown-sample-plugin.

Azure Document Intelligence
To use Microsoft Document Intelligence for conversion:

markitdown path-to-file.pdf -o document.md -d -e "<document_intelligence_endpoint>"


# Python API
Basic usage in Python:

from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("test.xlsx")
print(result.text_content)

# Document Intelligence conversion in Python:

from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("test.pdf")
print(result.text_content)
"""
