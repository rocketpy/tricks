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

# Process the dataset - tokenize the context texts (using a tokenizer from the Transformers library)
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

tokenized_dataset = squad_dataset.map(lambda x: tokenizer(x['context']), batched=True)


# If the dataset is bigger than disk or if don't want to wait to download the data, you can use streaming!!!

# If you want to use the dataset immediately and efficiently stream the data as you iterate over the dataset
image_dataset = load_dataset('cifar100', streaming=True)
for example in image_dataset["train"]:
    break
