l =[12, 34, 56, 78, 90]
l1=[]
print(l)

print(bool(l1))  # This will raise an error because a list cannot be converted to an integer

s=str(l)
print(s)
print(type(s))

print(tuple(l))

list = [['miesh', 2], [3, 4], [5, 6]]
dt =dict(list)


data = {((1,2), 2), (3, 4), (5, 6)}

tp = dict(data)

print(tp)
data = {("name", "Mitesh"), ("age", 22), ("city", "Surat")}

result = dict(data)

print(result)

set2 = {((10,20), 1)}
print(dict(set2))