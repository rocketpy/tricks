from six.moves.urllib.parse import urlencode, quote
# possible to use for 2 and 3 Python version

data = {'some': 'query', 'for': 'encoding'}
urlencode(data)
# 'some=query&for=encoding'
url = '/some/url/with spaces and %;!<>&'
quote(url)
# '/some/url/with%20spaces%20and%20%25%3B%21%3C%3E%26'
