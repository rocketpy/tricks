#  Very fast JSON to view
# http://jsonviewer.stack.hu/


# parse a JSON
import json

json_string = '{...}'
json_dict = json.loads(json_string)
print(json_dict)

# parse and read a JSON file
with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)

# Pretty Print JSON data
print(json.dumps(fcc_data, indent=4))
print(json.dumps(fcc_data, indent=4, sort_keys=True))
