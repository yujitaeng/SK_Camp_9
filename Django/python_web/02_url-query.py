from urllib.parse import urlencode, urlparse, parse_qs

params = {'search': 'python', 'page': 1}    # search=python&page=1
print(urlencode(params))

url = f"https://example.com/search?{urlencode(params)}"
# url = f"https://example.com/search?search=python&page=1&page=2&page=3"
print(parse_qs(urlparse(url).query))
