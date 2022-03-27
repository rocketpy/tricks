import re
import requests


try:
    result = requests.get("https://www.whatismyip.org/")
    # IP by CSS-selector:  #collapse-menu > h3 > a
    # IP by xPath:  //*[@id="collapse-menu"]/h3/a
    IP = re.compile('(\d{1,3}\.){3}\d{1,3}').search(result.text).group()
    if IP != "":
        print(IP)
except:
    print('Some error !')
   

# get public ip address
from requests import get


ip = get('https://api.ipify.org').text
print(f'My public IP address is: {ip}')


# or
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
print('My IP address is: {}'.format(ip))

