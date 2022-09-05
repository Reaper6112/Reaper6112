#!/usr/bin/env python
# coding: utf-8

# In[32]:


import check
from typing import *

class Family:
    """Store information about the Family of a person."""
    name: str
    children: List['Family']

    def __init__(self, name: str, children: List['Family']):
        self.name = name
        self.children = children

    def __repr__(self):
        return "Family('{}', {})".format(self.name, self.children)

tully = Family('Hoster',
                 [Family('Lysa',
                         [Family('Robin', [])]),
                  Family('Edmure', []),
                  Family('Catelyn',
                         [Family('Robb', []),
                          Family('Sansa', []),
                          Family('Arya', []),
                          Family('Bran', []),
                          Family('Rickon', [])])])
example1 = Family('Ann',
                  [Family('Bob', [
                      Family('Cy', [Family('Di',[]), Family('Ed',[]), Family('Fox',[])]),
                      Family('Glen', [])]),
                   Family('Hi', [
                       Family('Io', [Family('Jo',[]), Family('Kim',[]), Family('Li',[])]),
                       Family('Mo', [])])])
example2 = Family('Nat',
                  [Family('Ollie', [
                      Family('Poe', []),
                      Family('Q', []),
                      Family('Ro', []),
                      Family('Sal', [])]),
                   Family('Tim', []),
                   Family('Uq', []),
                   Family('Volodymyr', [])])


## Define you function here.
def most_children(fam: List[(Family)]) -> Tuple:
    """Count how many children are in t and 
    Return the family member with the most amount of children along with the number of children they have.
    
    Requires:
        Atleast 1 member of the family must exist.
    """

    member = ""
    count = 0

    d_tot = 0

    for member in fam.children:
        c_mem = member
        c_tot = 0
        cn = 0


        for child in member.children:
            c_tot += 1
            cn = most_children(member)[0]


        if abs(c_tot) > d_tot:
            member = c_mem
            d_tot = c_tot
            count = d_tot

    return (count,member.name)

## Make sure you test thoroughly.  Here's a start.
## Examples:
check.expect("MCtu", most_children(tully), (5, "Catelyn"))
check.expect("MCt1", most_children(example1), (3, "Cy"))
check.expect("MCt2", most_children(example2), (4, "Nat"))


# In[ ]:





# In[ ]:




