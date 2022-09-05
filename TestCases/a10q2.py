#!/usr/bin/env python
# coding: utf-8

# In[25]:


from typing import *
import check
def even_odd(nums: List[int]) -> List[int]:
    answer = ([], [])
    while nums != []:
        last = nums.pop()
        if last % 2 == 0:
            answer[0].append(last)
        else:
            answer[1].append(last)
    return answer

def even_odd_recursive(nums: List[int]) -> List[int]:
    answer = ([],[])
    print(nums)
    if len(nums) != 0:
        
        last = nums[0]
        
        if last % 2 == 0:
            answer[0].append(last)
            print(answer[0])
        else:
            answer[1].append(last)
        
        nums.remove(last)
        even_odd_recursive(nums)
        
    return answer

r = even_odd([1,2,3,4,5])
check.expect("test1", even_odd_recursive([1,2,3,4,5]), r)


# In[ ]:




