#!/usr/bin/env python
# coding: utf-8

# ### Pivot Table
#     엑셀에서 pivot table 기능이 있는것처럼, 
#     Pandas에서도 이와 유사한 pivot_table함수를 제공한다.
#     
#     분석을 하다 보면 원본 데이터의 구조가 분석 기법에 맞지 않아서 
#     행과 열의 위치를 바꾼다거나, 특정 요인에 따라 집계를 해서 구조를 
#     바꿔주어야 하는 경우가 종종 발생하는데 이때 피봇함수를 이용해서
#     분석에 알맞는 구조로 데이타를 변경해서 사용한다.
# 
#     피봇함수은 DataFrame의 데이타를 Reshape 하는 방법중 하나이다.
#     
#     여러 컬럼을 index, values, columns 값으로 사용가능하다.
#     그룹연산과 함께 사용

# #### Reshaping Data By Pivoting( 데이타의 재구조화 )

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


# In[4]:


data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9062546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}

df1 = DataFrame(data)
df1


# In[13]:


#index, columns, values 매개변수..키워드 매개변수
df1.pivot_table(index=['도시'],columns=['연도'],values=['인구'])
#df1.pivot_table(index=['도시'],columns=['연도'],'인구')
df1.pivot_table('인구',index=['도시'],columns=['연도'])
df1.pivot_table('인구','도시','연도')

df1.pivot_table('인구','도시','연도',margins=True)


# In[15]:


df1['인구'].mean()


# In[17]:


df1.pivot_table('인구', index=['연도','도시'])


# In[19]:


df1.groupby(['연도','도시'])[['인구']].mean()


# ### 실전 데이터

# In[20]:


tipdf = pd.read_csv('../data/tips.csv')
tipdf.head(1)


# In[23]:


'''
해당 데이터 분석의 목표는 식사총대금 대비 팁의 비율이 어떤 경우에 가장 높은 지 찾는 것이
우선 식사대금과 팁의 비율을 나타내는 tip_pct컬럼을 하나 추가하자
'''
tipdf['tip_pct'] = round(tipdf['tip']/tipdf['total_bill'],2)
tipdf.tail()

tipdf.dropna(inplace = True)
tipdf.tail()


# In[26]:


# 1. tipdf 에서 day기준으로 그룹핑 --- index, columns, values?-->index
tipdf.pivot_table(index='day', aggfunc='mean').round(2)


# In[29]:


# 2. tipdf에서 성별, 흡연여부별 그룹핑...pivot_table()...소수점 2자리
tipdf.pivot_table(index=['sex','smoker']).round(2)


# In[32]:


'''
pivot_table(속성)
values: 채우고자 하는 값
index: 그룹핑 기준
columns: 컬럼값

'''
tipdf.pivot_table(values=['total_bill','tip'],
                 index=['sex','day'],
                 columns='smoker')


# In[34]:


tipdf.pivot_table('tip','sex','smoker',aggfunc='count',margins=True)


# In[35]:


## 문제1. 성별에 따른 평균 팁비율
tipdf.pivot_table('tip_pct','sex',aggfunc='mean')


# In[36]:


# 문제 1과 동일한 결과가 나오도록 groupby()를 사용하새요

tipdf.groupby('sex')[['tip_pct']].mean()


# In[39]:


tipdf.pivot_table('tip_pct', index=['sex','smoker'])


# In[43]:


tipdf.pivot_table('tip_pct', index=['sex','smoker'],plot(kind='bar'))
plt.show()


# In[44]:


'''
여성, 남성 | 흡연자, 비흡연자
각 그룹에서 가장 많은 팁과 가장 작은 팁의 차이를 알고싶다
어디서 팁을 주는 격차가 더 많이 벌어지는지...
사용자 정의 함수를 만들고
agg()/ apply() 함수에서 적용한다.
'''

def max_min_tip(x):
    return x.max() - x.min()

tipdf.groupby(['sex','smoker'])[['tip']].agg(max_min_tip)

