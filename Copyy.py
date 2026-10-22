# we cannot store the immutable objects in the same memory location.  
# we cannot modify the immutable objects.
a = 10
b = a

b = 20

print(a)
print(b)

print("---------------------------------------------------")

a = [10, 20]
b = a

b.append(30)

print(a)
print(b)

print("---------------------------------------------------")

a = "Hello"
b = a

b = "Python"

print(a)
print(b)