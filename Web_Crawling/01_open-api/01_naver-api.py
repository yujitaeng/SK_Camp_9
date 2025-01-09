import urllib.parse
import urllib.request

client_id = 'pp72EQUySxMQwq4i1HOM'
client_secret = 'PBuWltjwIH'

encText = urllib.parse.quote('오늘 점심')

# 요청 URL
url = 'https://openapi.naver.com/v1/search/news.json?query=' + encText
# url = 'https://openapi.naver.com/v1/search/news.xml?query=' + encText

# Request 객체 생성 -> 헤더 설정정
request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)

# 실제 요청 후 응답
response = urllib.request.urlopen(request)

print(response.getcode())  # getcode() : 응답 코드 변환

response_body = response.read()  # read() : 응답 내용 반환
print(response_body.decode('utf-8'))