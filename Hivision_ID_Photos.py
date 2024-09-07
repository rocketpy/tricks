# HivisionIDPhotos - aims to develop a practical intelligent algorithm for producing ID photos. 
# It uses a complete set of model workflows to recognize various user photo scenarios, perform image segmentation, and generate ID photos.

# https://github.com/Zeyi-Lin/HivisionIDPhotos
# https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/README_EN.md

# Features:
"""
Perform lightweight image segmentation (Only CPU is needed for fast inference.)
Generate standard ID photos and six-inch layout photos according to different size specifications
Provide beauty features (waiting)
Provide intelligent formal wear replacement (waiting)
"""

# Environment Dependencies and Installation
"""
Python >= 3.7 (The main test of the project is in Python 3.10.)
onnxruntime
OpenCV
Option: Linux, Windows, MacOS

# Installation

Clone repo
git clone https://github.com/Zeyi-Lin/HivisionIDPhotos.git
cd  HivisionIDPhotos

(Important) Install dependent packages
It is recommended to create a Python 3.10 virtual environment with conda and then execute the following command.

pip install -r requirements.txt
pip install -r requirements-app.txt

# Download Weight Files
Option 1: Script Download

python scripts/download_model.py
Option 2: Direct Download

Save in the project's hivision/creator/weights directory:

modnet_photographic_portrait_matting.onnx (24.7MB): Official weights from MODNet, Download
hivision_modnet.onnx (24.7MB): A matting model better suited for solid background swapping, Download
mnn_hivision_modnet.mnn (24.7MB): MNN converted matting model by zjkhahah, Download
rmbg-1.4.onnx (176.2MB): Open source matting model from BRIA AI, download it and rename it to rmbg-1.4.onnx.
"""
