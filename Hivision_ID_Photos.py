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

# CUDA 12.x, cuDNN 8
pip install onnxruntime-gpu==1.18.0

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


# ID Photo Production
# Input 1 photo to obtain 1 standard ID photo and 1 high-definition ID photo in 4-channel transparent png

# python inference.py -i demo/images/test.jpg -o ./idphoto.png --height 413 --width 295


# Run Gradio Demo
# python app.py

"""
Python Inference
Core parameters:

-i: Input image path
-o: Output image path
-t: Inference type, options are idphoto, human_matting, add_background, generate_layout_photos
--matting_model: Portrait matting model weight selection
--face_detect_model: Face detection model selection
More parameters can be viewed by running python inference.py --help
"""

# ID Photo Creation
# Input 1 photo to obtain 1 standard ID photo and 1 high-definition ID photo in 4-channel transparent PNG.

# python inference.py -i demo/images/test0.jpg -o ./idphoto.png --height 413 --width 295


# Portrait Matting
# Input 1 photo to obtain 1 4-channel transparent PNG.

# python inference.py -t human_matting -i demo/images/test0.jpg -o ./idphoto_matting.png --matting_model hivision_modnet


# Add Background Color to Transparent Image
# Input 1 4-channel transparent PNG to obtain 1 3-channel image with added background color.

# python inference.py -t add_background -i ./idphoto.png -o ./idphoto_ab.jpg -c 4f83ce -k 30 -r 1


# Generate Six-Inch Layout Photo
# Input 1 3-channel photo to obtain 1 six-inch layout photo.

# python inference.py -t generate_layout_photos -i ./idphoto_ab.jpg -o ./idphoto_layout.jpg --height 413 --width 295 -k 200

  
# ID Photo Cropping
# Input 1 4-channel photo (the image after matting) to obtain 1 standard ID photo and 1 high-definition ID photo in 4-channel transparent PNG.

# python inference.py -t idphoto_crop -i ./idphoto_matting.png -o ./idphoto_crop.png --height 413 --width 295
