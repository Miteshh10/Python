# // Built-in Functions in Python
# 1. append() - Adds an element to the end of a list.

A = [1, 2, 3]
A.append(4)
print(A)

# 2. insert() - Inserts an element at a specified index.

A.insert(1, 1.5)  # Inserts 1.5 at index 1
print(A)

# 3. pop() - Removes and returns an element from a list. By default, it removes the last item, but you can specify an index to remove a specific item.
A.pop()  # Removes and returns the last item
print(A)

# 4.remove() - Removes the first occurrence of a specified value from the list.

A.pop(1)  # Removes and returns the item at index 1
print(A)

A.remove(2)  # Removes the first occurrence of the value 2
print(A)

# append always add only one element at a time , if pass the 2 element it will give exception takes exactly one argument 
A.append([4,5])
print(A)

print(len(A))


b = [1, 2, 3,2, 'four', [10, 20, 30]]

print(b)  

b.remove(2)
print(b)  # Output: [1, 3, 'four', [10, 20, 30]]

# b.remove(4,5)  # This will raise a ValueError because [4, 5] is not in the list
# print(b)  # Output: [1, 3, 'four', [10, 20, 30]]

b.remove([10,20 , 30])  # This will remove the list [10, 20, 30] from b
print(b)  # Output: [1, 3, 'four']

c = [1, 2, 3, 'four', [10, 20, 30]]


c[4].remove(30)  # This will remove the value 20 from the nested list [10, 20, 30]
print(c)  # Output: [1, 2, 3, 'four',

