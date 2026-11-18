n = int(input("n:"))

a =0
b=1
while n>0:
    c=a+b
    a,b=b,a
    n-=1
print(f"nth position:{a}")