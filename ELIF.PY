# a = int(input("Enter a number: "))

# if a > 0:
#     print("Positive number")

# elif a < 0:
#     print("Negative number")

# else:
#     print("Number is zero")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("A is greatest")

elif b > a and b > c:
    print("B is greatest")

elif c > a and c > b:
    print("C is greatest")

else:
    print("Two or more numbers are equal or all are equal")