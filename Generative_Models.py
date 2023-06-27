# Generative Models by Stability AI

# https://github.com/Stability-AI/generative-models

# General Philosophy
# Modularity is king. This repo implements a config-driven approach where we build and combine submodules by
# calling instantiate_from_config() on objects defined in yaml configs. See configs/ for many examples.

# Installation:
git clone git@github.com:Stability-AI/generative-models.git
cd generative-models

# Setting up the virtualenv
# This is assuming you have navigated to the generative-models root after cloning it!!!

NOTE: This is tested under python3.8 and python3.10. For other python versions, you might encounter version conflicts!!!

# PyTorch 1.13

# install required packages from pypi
python3 -m venv .pt1
source .pt1/bin/activate
pip3 install wheel
pip3 install -r requirements_pt13.txt


PyTorch 2.0

# install required packages from pypi
python3 -m venv .pt2
source .pt2/bin/activate
pip3 install wheel
pip3 install -r requirements_pt2.txt
