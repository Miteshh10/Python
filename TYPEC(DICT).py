a = [["name", "Mitesh"], ["age", 22]]

b = dict(a)

print(b)
print(type(b))

a = {"name": "Mitesh", "age": 22}

print(list(a))

a = {"x": 19, "y": 39}

print(tuple(a))
print(tuple(a.values()))
print(tuple(a.items()))

a = {"x": 10, "y": 20}

print(set(a))