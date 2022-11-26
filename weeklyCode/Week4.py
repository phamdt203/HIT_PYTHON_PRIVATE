# add elements to set
a = {1, 2, 3, 4}
a.update([5, 6])
print(a) # {1, 2, 3, 4, 5, 6}


# add 1 elment to set
a = {1, 2, 3, 4}
a.add("bb")
print(a) # {1, 2, 3, 4, 'bb'}


# a.remove() and a.discard delete 1 item


# union in set
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
print(A | B)  # {'red', 'yellow', 'green', 'blue', 'orange'}
print(A.union(B)) #  {'red', 'yellow', 'green', 'blue', 'orange'}


# intersection in set
print(A & B) # {'red'}
print(A.intersection(B)) # {'red'}


# Difference in set
print(A - B) # {'blue', 'green'}
print(A.difference(B)) # {'blue', 'green'}


# Symmetric Difference in set
print(A ^ B) # {'blue', 'green', 'yellow', 'orange'}
print(A.symmetric_difference(B)) # {'blue', 'green', 'yellow', 'orange'}


# Set method
# all() : return True if all item in set is True
# any() : return True if any item in set is True
# sorted() : return a set was sorted


# Use get method in dictionary : return the value if the key exist, else return None
D = {'name' : 'Tien'}
print(D.get('name')) # Tien
print(D.get('Age'))  # None


# Remove item in dict
# pop() : remove by key
# popitem() : remove by item
# clear() : remove all