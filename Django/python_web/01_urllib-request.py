from urllib import request, parse

# 1. html 가져오기
url = "http://quotes.toscrape.com/tag/life/"

response = request.urlopen(url)
html = response.read().decode('utf-8')

with open('quotes_life.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('저장 완료')

# 2. get 방식 요청 보내기
import json

api_url = "https://jsonplaceholder.typicode.com/posts/1"
api_response = request.urlopen(api_url)
print(json.load(api_response))

# 3. post 방식 요청 보내기
post_data = parse.urlencode({'username':'admin', 'password':'1234'}).encode()
req = request.Request('https://httpbin.org/post', data=post_data)
res = request.urlopen(req)
print(res.read().decode('utf-8'))
