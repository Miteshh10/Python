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

# WAP to display grades based on student marks.
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 75 and marks < 90:
    print("Grade B")

elif marks >= 60 and marks < 75:
    print("Grade C")

elif marks >= 35 and marks < 60:
    print("Grade D")

elif marks >= 0 and marks < 35:
    print("Fail")

else:
    print("Invalid marks")