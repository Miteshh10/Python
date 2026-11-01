# operator are the special symbol which is use to preform the an operation on the operand 
# operator are the type of libary mean they can be utize to perfrom special task 
# complex data type doesnot support the divivison , comparison and bitwise operator

# arithmetic operator



l=[10,20,30]+[40,50,60]
print(l)

t =(10,20,30)+(40,50,60)
print(t)

s = "Hello" + "World"
print(s)

# p = "Hello" + 3
# print(p)

# set = {1,2,3} + {4,5,6}
# print(set)
# Traceback (most recent call last):
#   File "d:\Python\Op.py", line 14, in <module>
#     set = {1,2,3} + {4,5,6}
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 

# dict = {"a":1,"b":2} + {"c":3,"d":4}
# print(dict)

print("------------------------------")

#subtraction operator

l = 10.8 - (7+3j)
print(l)

seet= {1,2,3,9, 0,2,3,2,4} - {4,5,6}

print(seet)

I=2.5*2.5
print(I)

#Power

po = 2**(1)
print(po)
# ** is used for exponentiation, and it works with numeric datatypes. Boolean values also work because True behaves like 1 and False behaves like 0.

print("------------------------------")

#floor division operator

f =      (4)// True
print(f)

d= 10- True
print(d)

print("------------------------------")
#multiplication operator

mp = 'ho' * 2
print(mp)

lp = [1,2,3]*3
print(lp)

tp = (1,2,3)*3
print(tp)
# set = {1,2,3}*3
# print(set)


IO= 5=='5'
print(IO)

hi = [1,2,3] > [1,2,3,5]
print(hi)

AB ={"Nme":"Mohit",
      "Age":20,}

BA = {"Nae":"Mohit",
      "Age":20,}

print(AB==BA)


sett = {1,2,3,8} == {3,8,2,1}
print(sett)

lit = [1,2,3,4] == [4,3,2,1]
print(lit)