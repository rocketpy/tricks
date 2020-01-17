import json
import requests


url = "https://api.github.com"

response = requests.get(url)
print("Status code is : ", response.status_code)

response_json = response.json()
print(response_json)

#  working with JSON

#  save data to JSON
def storeJSON(fileName, data = {}):
    with open(fileName, 'w')  as fd:
        json.dump(data, fd, indent = 4, separators = (',', ': '))

# load data from a JSON file
def loadJSON(fileName):
    with open(fileName) as fd:
        data = json.load(fd)
        print(data)
    return data

if __name__ == '__main__':
    data = loadJSON('file_name.json')
    print(data['menu']['value'])        
    data['menu']['value'] = 'movie'
    storeJSON('file_name.json', data)
    print()
    loadJSON('file_name.json')
    print(data['menu']['value'])  
