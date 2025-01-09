# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from urllib.request import urlretrieve

# class NewsEntry:
#     def __init__(self, title, href, img_path):
#         self.title = title
#         self.href = href
#         self.img_path = img_path

#     def __repr__(self):
#         return f'NewsEntry<title={self.title}, href={self.href}, img_path={self.img_path}'
    
# # keyword = input('노래 검색 키워드 입력:')
# url = f'https://music.bugs.co.kr/chart?wl_ref=M_left_02_01'

# response = requests.get(url)

# html = response.text

# bs = BeautifulSoup(html, 'html.parser')

# bugs_charts = bs.select('table.trackList')
# # print(len(bugs_charts))

# bugs_list = []

# for i, bugs_chart in enumerate(bugs_charts):
#     a_tag = bugs_chart.select_one('a.trackInfo')
#     title = a_tag.text
#     href = a_tag['href']

#     img_tag = bugs_chart.select_one('img.thumbnail')
#     if img_tag:
#         img_lazysrc = img_tag['data-lazysrc']
#         if img_lazysrc.startswith('http'):
#             img_dir = 'images2'
#             today = datetime.now().strftime('%y%m%d')
#             filename = f'{img_dir}/{today}_{i}.jpg'
#             urlretrieve(img_lazysrc, filename)
#     else:
#         filename = 'empty'

#     bugs_entry = NewsEntry(title, href, filename)
#     bugs_list.append(bugs_entry)

# for bugs in bugs_list:
#     print(bugs)
    

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve

class MusicEntry:
    def __init__(self, title, artist, img_path):
        self.title = title
        self.artist = artist
        self.img_path = img_path

    def __repr__(self):
        return f'{self.artist}의 {self.title} | {self.img_path}'
    
# 1. request 로 url get해오기
response = requests.get('https://music.bugs.co.kr/chart')

# 2. response를 html 로 받기 -> BeautifulSoup 객체 생성
bs = BeautifulSoup(response.text, 'html.parser')

# 3. table.trackList 목록 > a.thumbnail img: 앨범커버 이미지, p.title a text: 앨범 제목
track_list = bs.select('table.trackList tbody tr')

result_list = []
for i, song in enumerate(track_list[:30]):  # 30개로 슬라이싱, enumerate 인터럴하게 인덱스를 받아올 수 있음
    title = song.select_one('p.title a').text
    artist = song.select_one('p.artist a').text
    # print(title, artist) -> 중간 점검 출력용

    # 4. 앨범커버 이미지 저장
    img_src = song.select_one('a.thumbnail img')['src']
    filename = f'album_images/{datetime.now().strftime('%y%m%d_%H%M%S')}_{i+1}.jpg'
    urlretrieve(img_src, filename)

    music_entry = MusicEntry(title, artist, filename)
    result_list.append(music_entry)


# 5. 30위까지 출력
for result in result_list:
    print(result)