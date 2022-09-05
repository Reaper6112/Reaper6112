#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import *
import check

def slowfunc(L: List[int]) -> List[int]:
    """You do not need to write a docstring for slowfunc or fastfunc."""
    ans = []
    for i in range(len(L)):
        x = L.pop(0)
        m = 0
        for j in range(1, 5):
            m = m + x**j
        ans = ans + [x, x**2]
    return ans

def fastfunc(L: List[int])->List[int]:
    ans = []
    for i in range(len(L)):
        
        x = L[0]
        
        L.remove(x)
        
        ans = ans + [x, x**2]
        
    return ans


# In[ ]:




