#  Using a pickle, to save cookies as text file and load it later !

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)
           
        
# Using JSON
import json
from selenium import webdriver


#  get cookies
driver = webdriver.Chrome()
driver.get("https://www...")
cookies = driver.get_cookies()
with open('cookies.json', 'w', newline='') as outputdata:
    json.dump(cookies, outputdata)
            
        
#  to send cookies
import json
from selenium import webdriver


with open('cookies.json', 'r', newline='') as inputdata:
    cookies = json.load(inputdata)
curcookie = cookies[0]
driver = webdriver.Chrome()
driver.get("https://www...")
driver.add_cookie(curcookie)
