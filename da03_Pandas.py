#!/usr/bin/env python
# coding: utf-8

# ### Pandas
#     pandas는 Panel Datas의 약자
#     파이썬을 이용한 데이터 분석에서 가장 많이 사용되는 라이브러리
#     
#     Pandas 자료구조
#     1. Series - 1차원 배열(벡터)
#     
#     2. DataFrame - 2차원 배열(매트릭스) 가장 중요(표형식):엑셀
#     
#     3. Panel - 3차원(대상아님)

# #### Series
#     시리즈 생성, 구조확인

# In[4]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


# In[6]:


get_ipython().run_line_magic('pinfo', 'Series')


# In[12]:


ser1 = Series(np.random.randint(10,20,5))
ser1
print(ser1.index)
print(ser1.values)
print(ser1.dtype)
print(ser1)


# ### 시리즈값 조회하기
#     단일값을 선택하거나 여러값을 선택할 때
#     1) 인덱스로 라벨을 사용할 수 있다.
#     
#     2) 슬라이싱 방법
#         -라벨 사용 : 마지막 라벨 포함됨 ['a' : 'd']
#         -숫자 사용 : 마지막 숫자 포함 안 됨

# In[15]:


ser1


# In[19]:


ser1[0]
#ser1['a']

print(ser1[1:4])
#print(ser1['b':'d'])


# In[24]:


# 응용해서 조회하기 : 아래 두 표기법을 구분하자
ser1[:2]
print(ser1)
ser1_1 = ser1[::2]
print(ser1_1)


# In[25]:


#시리즈 간의 연산

resSer = ser1+ser1_1
print(resSer)


# ### 누락 데이터 조회하기
#     
#     

# In[27]:


resSer


# In[32]:


print(resSer.isnull())
print(resSer[resSer.isnull()])
print(resSer.notnull())
print(resSer.isnull().sum())

