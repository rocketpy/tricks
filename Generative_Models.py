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

# NOTE: This is tested under python3.8 and python3.10. For other python versions, you might encounter version conflicts!!!

# PyTorch 1.13
# install required packages from pypi
python3 -m venv .pt1
source .pt1/bin/activate
pip3 install wheel
pip3 install -r requirements_pt13.txt


# PyTorch 2.0
# install required packages from pypi
python3 -m venv .pt2
source .pt2/bin/activate
pip3 install wheel
pip3 install -r requirements_pt2.txt

# Dataset Handling
example = {"jpg": x,  # this is a tensor -1...1 chw
           "txt": "a beautiful image"}

# Training:
"""
We are providing example training configs in configs/example_training. To launch a training, run

python main.py --base configs/<config1.yaml> configs/<config2.yaml>
where configs are merged from left to right (later configs overwrite the same values).
This can be used to combine model, training and data configs. However, all of them can also be defined in a single config.
For example, to run a class-conditional pixel-based diffusion model training on MNIST, run

python main.py --base configs/example_training/toy/mnist_cond.yaml
"""
