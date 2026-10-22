# we cannot store the immutable objects in the same memory location.  
# we cannot modify the immutable objects.
a = 10
b = a

b = 20

print(a)
print(b)