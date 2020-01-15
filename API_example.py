import requests


url = "https://api.github.com"

response = requests.get(url)
print("Status code is : ", response.status_code)

response_json = response.json()
print(response_json)
