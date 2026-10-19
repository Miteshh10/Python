s = "123"
c="(4+5j)"
print(s)

print(int(s))  # This will raise an error because 'Mitesh' cannot be converted to an integer
print(float(s))

print(complex(c))
print(bool(s))
l = "MITESH"
print(list(l))

T = "RITESH"
print(tuple(T))

S = "MALAYLAM"
s1=123124562928
print(set(S))
print(set(s1))  # This will raise an error because a string cannot be converted to a dictionary

d=[(1,"mitesh"),(1.0,4+5j),( 1+2j,'mitesh'), (True,30), ('lo','lo'), ((90,12,78),[1,2,3])]
print(dict(d)) 

# string can be converted into 
# int : string should be in number format,
#  float, complex, bool, list, tuple, set and dict
