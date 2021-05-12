#!/usr/bin/env python
# coding: utf-8

# ### Numpy
#     Numeric Python의 약자
#     수학분야 관련 통계 연산작업시 사용
#     과학 계산 컴퓨팅, 데이터 분석에 필요한 기본적인 패키지
#     
#     Numpy 배열은 리스트와 거의 흡사
#     리스트보다 훨씬 빠르고 메모리 효율성이 높아서 성능상 우위를 차지한다.
#     
#     Numpy는 사용에 앞서서 import해서 사용해야 한다.
#     Numpy 배열 만드는 방법
#     1) array() 사용
#     2) random 모듈의 랜덤함수 사용

# In[2]:


import numpy as np


# #### np 배열 생성 | 리스트와 비교
#     array() 함수 사용
#     

# In[11]:


myList = [4,5,6,7]
myArr = np.array(myList)

print(myList)
print(myArr)

print(type(myList))
print(type(myArr))

'''
nparray는 출력결과 [] 안에 값들이 나열되지만 ,로 구분되진 않는다.
ndarray타입
ndarray 클래스는 다차원행렬구조를 지원하는 Numpy의 핵심 클래스
'''

myList_sub = myList[1:3]
print(myList_sub)

myArr_sub = myArr[1:3]
print(myArr_sub)

print('*'*30)
'''
리스트는 원본 안바뀐다. 변경되면 기존의 것을 카피해놓고 새로운 것을 만든다.
반면에, np배열은 원본뷰가 바뀌어버린다.
이것이 리스트와 np배열의 가장 큰 차이점이다.

'''

print(myList)
print(myArr)


# In[14]:


#rand() 함수 사용하기
 
a = np.random.rand(5)
print(a)
print(type(a))

b = np.random.randint(1,10)
print(b)
print(type(b))


# ### np배열의 초기화
#     zeros(), ones(), arange()..함수를 이용해서 배열 생성과 동시에 특정한 값으로 초기화 할 수 있다.

# In[23]:


#1.
az = np.zeros(10)
print(az)

#2. 1값으로 이뤄진 크기가 10인 배열 생성
ao = np.ones(10)
print(ao)

#3. 3 by 3 (3행 3렬)단위 배열 생성
ae = np.eye(3)
print(ae)

#4. arange()
print(np.arange(3))
print(np.arange(3,7))
print(np.arange(3,10,2))


# ### np배열과 리스트의 차이점
#     1. np배열은 원본을 바로 바꿈으로써 메모리 효율성이 뛰어나다.
#     2. 리스트는 여러가지 자료형이 원소로 올 수 있지만, np배열은 한가지 자료형만 원소로 쓰일 수 있다.
#     

# In[30]:


L = [1,2,3,'4',4,'하바리'] #리스트는 서로 다른 자료형이 원소로 올 수 있다.
print(L)
print(type(L))

A = np.array(L)#하나의 자료형으로 통일되어 저장됨(capacity가 더 큰 자료형으로 변환됨)
print(A)

A2 = np.array([1,5,6,4,3.4])
print(A2)

A3 = np.array([1,2,3,4],dtype='float')
print(A3)

A4 = np.array([1,2,3,4],dtype = np.float64)
print(A4)


# ### Numpy 배열에서 사용되는 함수, 속성
#     ndim shape reshape size type dtype

# In[33]:


arr1 = np.array([[1.0,2,3],[4,5,6]])
arr1


# In[34]:


print(type(arr1))
print(np.ndim(arr1))
print(np.shape(arr1))
print(np.size(arr1))

print('*'*30)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)

