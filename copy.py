a = [10, 20, 30]

b = a

b.append(40)

print("a =", a)
print("b =", b)


a = [10, 20, 30]

b = a.copy()

b.append(40)

print("a =", a)
print("b =", b)

import copy

a = [[10, 20], [30, 40]]

b = copy.deepcopy(a)

b[0].append(99)

print("a =", a)
print("b =", b)