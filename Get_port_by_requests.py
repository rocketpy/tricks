#  resp = requests.get(http://blabla.com:8080)

# for standard port
url = 'https://...'
resp = requests.get(url, verify=False, timeout=2)
print(resp.text)


adapter = requests.adapters.HTTPAdapter(max_retries=1)
resp_res = {'lines': 0, 'resp_code': 0, 'port': 'N/A', 'history': [], 'final_url': ''}
session = requests.Session()
url_1 = 'https://...'

session.mount(url01, adapter)

try:
    resp = session.get(url_1, verify=False, timeout=2)
    resp_soup = BeautifulSoup(resp.text, "html.parser")
except (requests.ConnectionError, requests.HTTPError, requests.Timeout,
        requests.TooManyRedirects) as e:
            logging.error('scrap_website - HTTPS connection failed')
            logging.error(e)
else:
    resp_res['lines'] = len(str.splitlines(str(resp_soup.prettify())))
    resp_res['resp_code'] = resp.status_code
    resp_res['port'] = 'HTTPS'
    resp_res['history'] = resp.history
    resp_res['final_url'] = resp.url

        
