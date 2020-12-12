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
from selenium import webdriver
import json


#  get cookies
driver = webdriver.Chrome()
driver.get("https://")
cookies = driver.get_cookies()
with open('cookietest.json', 'w', newline='') as outputdata:
    json.dump(cookies, outputdata)
            
            
