"""
Need to use: execute_cdp_cmd()
With execute_cdp_cmd(cmd, cmd_args) we can execute google-chrome-devtools commands using Selenium.
We can modify the user-agent easily to prevent Selenium from getting detected.
"""
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
print(driver.execute_script("return navigator.userAgent;"))
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                                                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                                                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get('https://www.httpbin.org/headers')

"""
driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_1"}})
# driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_2"}})
# driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_3"}})
driver.get('https://www.httpbin.org/headers')
"""

ua = UserAgent()
chrome_options = Options()
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument("--start-maximized")

u_agents = []

for agent in u_agents:
    # user_agent = ua.random
    # chrome_options.add_argument()
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_1"}})
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:...")
    driver.get('https://www...')
    time.sleep(2)
