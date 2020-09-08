"""
Homework assignment for the 'Python is easy' course by Pirple.

Function that returns True if 2 or more of the parameters are equal,
and false is none of them are equal to any of the others.
"""

def atLeastTwoAreEqual(First, Second, Third):
    if int(First) == int(Second):
        return True
    elif int(First) == int(Third):
        return True
    elif int(Second) == int(Third):
        return True
    else:
        return False
