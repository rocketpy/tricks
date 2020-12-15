#  PyPi:  https://pypi.org/project/fake-useragent/

from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


options = Options()
ua = UserAgent()
userAgent = ua.random  #  best one, random via real world browser usage statistic
# print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\\chromedriver.exe')
driver.get("https://www...")

driver.quit()


#  If You don’t want cache database or no writable file system:
from fake_useragent import UserAgent

ua = UserAgent(cache=False)
