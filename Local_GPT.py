# localGPT - This project was inspired by the original privateGPT. 

# https://github.com/PromtEngineer/localGPT
# Video - https://www.youtube.com/watch?v=MlyoObdIHyo

"""
Install conda
conda create -n localGPT

Activate
conda activate localGPT

pip install -r requirements.txt
Then install AutoGPTQ - if you want to run quantized models for GPU

git clone https://github.com/PanQiWei/AutoGPTQ.git
cd AutoGPTQ
git checkout v0.2.2
pip install .
"""

# Ask questions to your documents, locally!

# In order to ask a question, run a command like:
python run_localGPT.py

# And wait for the script to require your input.
> Enter a query:

# Run the UI
"""
Start by opening up run_localGPT_API.py in a code editor of your choice. If you are using gpu skip to step 3.

If you are running on cpu change DEVICE_TYPE = 'cuda' to DEVICE_TYPE = 'cpu'.

Comment out the following:
model_id = "TheBloke/WizardLM-7B-uncensored-GPTQ"
model_basename = "WizardLM-7B-uncensored-GPTQ-4bit-128g.compat.no-act-order.safetensors"
LLM = load_model(device_type=DEVICE_TYPE, model_id=model_id, model_basename = model_basename)
Uncomment:
model_id = "TheBloke/guanaco-7B-HF" # or some other -HF or .bin model
LLM = load_model(device_type=DEVICE_TYPE, model_id=model_id)
If you are running gpu there should be nothing to change. Save and close run_localGPT_API.py.
Open up a terminal and activate your python environment that contains the dependencies installed from requirements.txt.

Navigate to the /LOCALGPT directory.

Run the following command python run_localGPT_API.py. The API should being to run.

Wait until everything has loaded in. You should see something like INFO:werkzeug:Press CTRL+C to quit.

Open up a second terminal and activate the same python environment.

Navigate to the /LOCALGPT/localGPTUI directory.

Run the command python localGPTUI.py.

Open up a web browser and go the address http://localhost:5111/.
"""
