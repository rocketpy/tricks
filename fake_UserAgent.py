from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


options = Options()
ua = UserAgent()
userAgent = ua.random
# print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\\chromedriver.exe')
driver.get("https://www...")

driver.quit()
