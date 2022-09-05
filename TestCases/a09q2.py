#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import *
import check

LLT = Union[int, List['LLT']]


## Define you function here.
def tree_map(t: LLT, f: Callable)-> LLT:
    """Return a new LLT object where each element is processed by the given function.
    
    Reequires:
        
        t must be an LLT object.
        
        f must be a defined Callable function.
    """
    if isinstance(t, int):
        t = f(t)
    else:
        
        for item in t:

            item = tree_map(item, f)
            

        return t


def add1(x: int) -> int: return x + 1
def sqr(x: int) -> int: return x*x
def double(n: int) -> int: return n * 2

## Make sure you test thoroughly.  Here's a start.
## Examples:
check.expect("TM1",
             tree_map([2, [[4], 6], 0, [1]], add1), [3, [[5], 7], 1, [2]])
check.expect("TM2",
             tree_map([2, [[4], 6], 0, [1]], double), [4, [[8], 12], 0, [2]])
check.expect("TM3", tree_map(7, sqr), 49)
check.expect("TM4", tree_map([[[[[[[7]]]]]]], add1), [[[[[[[8]]]]]]])


# In[ ]:




