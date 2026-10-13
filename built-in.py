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

# append always add only one element at a time , if pass the 2 element it will give exception takes exactly one argument 
A.append([4,5])
print(A)

print(len(A))