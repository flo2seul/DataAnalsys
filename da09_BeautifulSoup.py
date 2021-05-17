#!/usr/bin/env python
# coding: utf-8

# ### BeautifulSoup
#     BeautifulSoup은 HTML과 XML 문서를 파싱하기 위한 파이썬 라이브러리
#     
#     BeautifulSoup parser를 사용해서 HTML 문서 내 태그를 구조화하고 파이썬 객체로 만들어서 원하는 태그를 찾을 수 있도록 도와준다.
#     
#     BeautifulSoup 라이브러리는 외부 라이브러리이기 때문에 사용하기 위해서는 설치부터 해야한다.(라이브러리는 이미 설치되어 있음)
#     BeautifulSoup 인터넷 홈페이지 내용을 구조화해서 가져오는 모듈

# In[2]:


get_ipython().system('pip install beautifulsoup4')


# ### 1. 네이버 URL 정보를 가져옴 - requests.get()
# ### 2. BeautifulSoup을 이용해서 파싱함

# In[7]:


import requests
from bs4 import BeautifulSoup

req = requests.get("http://naver.com")#네이버 url 정보를 가져온다.
html = req.text

soup = BeautifulSoup(html, 'html.parser')#BeautifulSoup을 이용해서 html.parser 파싱
#print(soup.prettify())


# ### 3. BeautifulSoup find() 단수, find_all() 복수

# In[9]:


result = soup.find_all('a','thumb') #태그와 특정 클래스등을 참조한다.
#result

news_list = []
for i in result:
    news_list.append(i.find('img')['alt'])#img태그안에 있는 alt속성의 값을 추가
print(news_list)


# In[18]:


#BeautifulSoup이 가지고있는 특정 함수들...
soup.title
soup.title.name
soup.title.string

# 태그가 여러개 있더라도 항상 첫번째 태그만 가져와서 검색한다...주의
soup.img
#soup.img['alt']
#soup.img['class'] class 속성이 첫번째 img 태그에는 없기 때문에 에러난다.
soup.img['height']

import re #정규식 표현관련 모듈...특정 단어가 얼마나 들어있는 지 확인
print(soup.find_all(string=re.compile("네이버")))


# ### BeautifulSoup의 select_one(), select()
#     find(), find_all() ----태그 기반 검색
#     select_one(), select() ----선택자 기반 검색

# In[19]:


'''
이 부분만 보면 find(), find_all() 함수와 별다른 차이점이 없어보인다.
조금 더 아래 예제를 해보자
'''
print(soup.select_one('a')) #a 태그 하나만 가져옴
print(soup.select('a'))#a 태그 다 가져옴


# In[22]:


#css 선택자 사용하는 기법 그래도 사용한다.
body = soup.select('body a')
#body

ul = soup.select('div>ul')
ul


# ### BeautifulSoup get_text(), get()
#     get_text() --- 

# In[ ]:


text.get_text()
text.get('class')


# ### BeautifulSoup 사용해서 네이버 영화 랭킹 가져오기
#     1. 네이버 영화랭킹 홈페이지 접속 url, text 가져오기
#     https://movie.naver.com/movie/sdb/rank/rmovie.nhn
#     2. 분석 작업을 하기 위해서 BeautifulSoup을 만들고 html 파서로 파싱
#     3. 리턴된 soup객체를 분석한 결과로 영화랭킹을 찾아서 출력
#     select(), find_all

# In[23]:


import requests
from bs4 import BeautifulSoup


# In[24]:


# 1. 특정 사이트 url 받아와서...request.get('')
req = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
html = req.text

# 2. 분석 작업을 하기 위해서 bs생성
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


#3. soup 객체를 분석해서 영화랭킹을 찾아본다.(영화랭킹 태그가 어떤 구조로....)
'''
영화랭킹 태그 구조는 
div 태그의 클래스 속성의 값이 tit3
a 태그들이 계속 반복되는 구조...
'''
movie_ranking_list = soup.find_all('div'.class_='tlt3')
for i in range(movie_ranking_list):
    print("{:2}위 :{}".foramt(i+1, movie_ranking)


# In[ ]:





# In[ ]:





# In[ ]:




