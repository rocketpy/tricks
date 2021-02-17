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