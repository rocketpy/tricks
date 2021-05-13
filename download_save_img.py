import requests

r = requests.get('https://  .png')
with open('file_name.png', 'wb') as f:
    f.write(r.content)


# checking status code and path to file
import requests

picture_request = requests.get(Photo_URL)
if picture_request.status_code == 200:
    with open("/path/to/image.jpg", 'wb') as f:  # or 'file_name.png'
        f.write(picture_request.content)

