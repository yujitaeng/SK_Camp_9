import urllib.parse
import urllib.request
import json
import mysql
import mysql.connector

client_id = 'pp72EQUySxMQwq4i1HOM'
client_secret = 'PBuWltjwIH'

encText = urllib.parse.quote('베스트셀러')

# 요청 URL
url = 'https://openapi.naver.com/v1/search/book.json?query=' + encText

# Request 객체 생성 -> 헤더 설정정
request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)


# 실제 요청 후 응답
response = urllib.request.urlopen(request)

print(response.getcode())  # getcode() : 응답 코드 변환

response_body = response.read()  # read() : 응답 내용 반환
response_body = json.loads(response_body)

book_list = response_body['items']

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'squirrel',
    password = 'squirrel',
    database = 'bookdb'
)

cursor = connection.cursor()

sql = 'INSERT INTO naver_book (book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES (%s, %s, %s, %s, %s, %s, %s)'

for book_info in book_list:
    values = (book_info['title'], book_info['image'], book_info['author'], book_info['publisher'], str(book_info['isbn']), book_info['description'], book_info['pubdate'])
    cursor.execute(sql, values)

connection.commit()

cursor.close()
connection.close()