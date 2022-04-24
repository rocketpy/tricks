"""
Need to use: execute_cdp_cmd()
With execute_cdp_cmd(cmd, cmd_args) we can execute google-chrome-devtools commands using Selenium.
We can modify the user-agent easily to prevent Selenium from getting detected.
"""

driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_1"}})
# driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_2"}})
# driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser_3"}})
driver.get('https://www.httpbin.org/headers')
