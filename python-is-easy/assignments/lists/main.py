'''
Homework assignment for the 'Python is easy' course by Pirple.
'''

myUniqueList = []

'''
Anything that's passed to this function gets added to myUniqueList,
unless its already exists in myUniqueList.
If the element exists in the myUniqueList, it's not added, and the function
returns False.
The function returns True when the element got added to the list.
'''
def addToMyListOrReject(element):
    if element in myUniqueList:
        return False
    else:
        myUniqueList.append(element)
        return True

# Tests

addToMyListOrReject(1)
addToMyListOrReject(2)
addToMyListOrReject(2)
addToMyListOrReject(3)
addToMyListOrReject(3)
addToMyListOrReject(3)
addToMyListOrReject(2)
addToMyListOrReject(1)

print(myUniqueList)

# Extra credit
        
myLeftovers = []

'''
Anything that's passed to this function gets added to myUniqueList,
unless its already exists in myUniqueList.
If the element exists in the myUniqueList, it's added to myLeftovers list,
and the function returns False.
The function returns True when the element got added to the myUniquieList.
'''
def addToMyList(element):
    if element in myUniqueList:
        myLeftovers.append(element)
        return False
    else:
        myUniqueList.append(element)
        return True
