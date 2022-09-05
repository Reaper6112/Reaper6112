#!/usr/bin/env python
# coding: utf-8

# In[13]:


import check
from typing import *
import math


def zero(f: Callable, x0: float, x1: float) -> float:
    """Return a value between x0 and x1 such that the function f(x)
    returns a value that is close to 0 within 0.0001

    Requires:
      f is continuous on [x0, x1)
      f(x0) and f(x1) have opposite signs
      x0 <= x1
    """
    if abs(f(x0)) > 0.0001:
        mid_point = (x0 + x1) / 2

        if f(mid_point) * f(x0) < 0:
            x1 = mid_point
            x0 = zero(f,x0,x1)
            
        else:
            x0 = mid_point
            x0 = zero(f,x0,x1)

    return x0


def cubic(x: float) -> float: return (x-8)*(x-9)*(x-12.345)
check.within('Example 1', zero(cubic, 7.0, 15.0), 12.345, 0.0001)

check.within('cos', zero(math.cos, 0.0, 4.0), math.pi/2, 0.0001)
check.within('sin, passing 0 repeatedly',
             zero(math.sin, 2.4, 10.4), 3*math.pi, 0.0001)
def forth_pow_poly(x: float) -> float:
    return x * (x+1.217) * (x-5.432) * (x+6.345)
check.within('fourth power polynomial, -to+',
             zero(forth_pow_poly, -6.0, -0.1), -1.217, 0.0001)
check.within('fourth power polynomial, +to-',
             zero(forth_pow_poly, -1.0, 5.0), 0.0, 0.0001)
def linear(x: float) -> float: return x+5
check.within('when first midpoint is already 0',
             zero(linear, -8.0, -2.0), -5.0, 0.0001)
check.within('when first midpoint is not 0',
             zero(linear, -100.0, -2.0), -5.0, 0.0001)


# In[ ]:




