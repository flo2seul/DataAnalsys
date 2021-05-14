#!/usr/bin/env python
# coding: utf-8

# ### 랜덤함수와 seed값 설정하기
#     seed값은 한번만 설정해주면 계속 적용된다.
#     시드는 보통 현재시각등을 이용해서 자동으로 정해지지만
#     우리가 수동으로 설정할 수 있다.
#     특정한 시드값이 사용되면 그 다은에 만들어지는 난수들을 예측할 수 있다.

# In[1]:


import numpy as np


# In[2]:


np.

arr1 = np.random.randn(4,4)
arr1


# In[6]:


arr2 = np.arange(1,10)
arr2

arr3 = np.arange(1,10).reshape(3,3)
arr3


# ### 인덱싱, 슬라이싱

# In[9]:


narray = np.arange(5)
narray


# In[11]:


narray2 = np.random.randint(10,20,16).reshape(4,4)
narray2


# In[18]:


#1) narray2 중에서 첫번째 행의 세번째 값 12를 가져오려면?
narray2[0][2]
narray2[0,2]

#2) 2번째 라인 [10,14,15,15] 전체를 출력
narray2[1:2,0:4]
narray2[1:2,:]
narray2[1,:]
narray2[1,0:]

#3) 전체 행에 대해서 4번째 열을 출력?
narray2[0:4, 3:4]
narray2[0:, 3:4]
narray2[:,3]

#4) 전체 행에 대해서 1,2번째까지의 열을 출력
narray2[:,:2]


# ### 인덱싱과 조건 슬라이싱

# In[21]:


arr1
#1. 논리연산자 사용해서 값을 받아오거나 값을 변경

arr1[arr1>0]
arr1[arr1<0]
arr1[arr1<0] = 0
#원본도 함께 바뀐다
arr1


# In[23]:


#2. where 함수
arr1_1 = np.where(arr1>0, arr1, -1)
arr1_1


# In[25]:


#3. 1,2를 가지고 응용하기
arr2 = np.array([[1,2],[3,4],[5,6]])
arr2


# In[28]:


bool_idx = arr2>2
print(bool_idx)

print(arr2[bool_idx])


# ### 통계 함수
#     sum, mean, max, argmin, argmax, cumsum

# In[33]:


narray2


# In[36]:


np.sum(narray2)
print(np.sum(narray2, axis=1))
print(np.sum(narray2, axis=0))

