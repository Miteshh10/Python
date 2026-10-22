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

a = {10, 10, 30, 50, 20, 30}
b = a

b.add(40)

print(a)
print(b)