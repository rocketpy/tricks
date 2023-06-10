# The largest hub of ready-to-use datasets for ML models with fast, easy-to-use and efficient data manipulation tools

# https://github.com/huggingface/datasets
# huggingface.co/docs/datasets

# Installation
# pip install datasets

# With conda
# conda install -c huggingface -c conda-forge datasets

# Usage
datasets.list_datasets() to list the available datasets
datasets.load_dataset(dataset_name, **kwargs) to instantiate a dataset

# Example
from datasets import list_datasets, load_dataset

# Print all the available datasets
print(list_datasets())

# Load a dataset and print the first example in the training set
squad_dataset = load_dataset('squad')
print(squad_dataset['train'][0])

# Process the dataset - add a column with the length of the context texts
dataset_with_length = squad_dataset.map(lambda x: {"length": len(x["context"])})
