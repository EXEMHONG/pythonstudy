# 웹 크롤링
# : 웹 사이트로 부터 데이터를 수집하는 과정

# 라이브러리 설치
# 터미널 
# pip install requests
# pip install beautifulsoup4
# pip install lxml


import requests
from bs4 import BeautifulSoup

# 특정 사이트의 html(웹 사이트 문서) 가져오기
url = "https://sports.news.naver.com/news?oid=109&aid=0005045118"
html = requests.get(url)

print(html)

# 상태코드
# 200 응답 성공
# 404 페이지 없음
# 500 서버 없음

# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 스포츠 기사제목
h4 = soup.find('h4', class_='title')
print(h4)

# 생성 일자
div = soup.find('div', class_='info')
print(div)

# 기사
article = soup.find('div', id="newsEndContents")
print(article.get_text())

#strong = span.find('strong', class_='_text')
#print(strong)
'''
    <strong class="_text">아바타: 물의 길</strong>
'''

#movie_title = strong.get_text()
#print(movie_title)
'''
    # 아바타: 물의 길
'''

