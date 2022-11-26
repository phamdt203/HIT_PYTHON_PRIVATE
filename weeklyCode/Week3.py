# Use del command to delete the elements that you know correctly
myList = ["physics", "chemistry", 1997, 2000]
del myList[1] # Delete "chemistry"
print(myList) # ["physics", 1997, 2000]


# Use remove method if you don't know that element correctly
myList.remove(1997)
print(myList) # ["physics", 2000]


# Reverse list with slicing
L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])
# ['e', 'd', 'c', 'b', 'a']


# Change elements
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L) # ['a', 1, 2, 3, 'c', 'd', 'e']


# Append elements
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3] # L[i:i]
print(L) # [1, 2, 3, 'a', 'b', 'c']


# Remove elements
L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []  # = del L[1:5]
print(L) # ['a']


# Clone or Copy in List
# if you assign new_List = old_List, you don't have two different list
# you still have one list that two lists above reference to
old_List = ['red', 'green', 'blue']
new_List = old_List
new_List[0] = 'xx'
print(old_List) # ['xx', 'green', 'blue']
print(new_List) # ['xx', 'green', 'blue']


# List method
# clear() : delete all elements
# copy() : copy 1 list
# count(item) : count number of item in list
# extend() : add 1 element or another list at the end of the list
# insert(index, item) : add item at index spot
# pop() : delete a element at the end of list
# remove(item) : delete first appearance of item
# reverse() : reverse the list
# sort() : sort the list