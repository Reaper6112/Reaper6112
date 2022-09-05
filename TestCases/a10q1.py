#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import check
## Every function below can be described by one of these.
## Set each value r1, r2, r3 to one one these.
runtimes = ("1", "log n", "sqrt n", "n", "n**2", "n**3", "2**n")

def f1(L):
    ans = 0
    while L != []:
        ans = ans + L[0]
        L = L[1:]
    return ans > 100
## Assign values to r1 and e1 to submit your answer for f1.
r1 = "n"
e1 = """Because the at the end of the loop L is set to [0], it runs only once. 
    Everything else except L = L[1:] has runtime O(1) while this line has O(1)"""
check.expect("f1", r1 in runtimes, True)


def f2(L):
    if len(L) == 0:
        return ""
    else:
        return f2(L[1:]) + f2(L[:-1])
## Assign values to r2 and e2 to submit your answer for f2.
r2 = "n**2"
e2 = """The if statement has O(n) due to len. The else statement has O(n) + O(n) = O(n^2).
    together O(n) + O(n^2) = O(n^2)"""
check.expect("f2", r2 in runtimes, True)


def f3(L):
    ans = 1
    for x in L[:min(len(L), 16)]:
        if x%10==1:
            ans = ans + 1
        else:
            ans = ans + 2
    return ans
## Assign values to r3 and e3 to submit your answer for f3.
r3 = "n**2"
e3 = """The ans assignments are O(1). The if else statement is O(n) . O(1) . O(n) = O(n^2)"""
check.expect("f3", r3 in runtimes, True)

