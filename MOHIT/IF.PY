#syntax : if condition: 
#The if statement is a conditional statement used to execute a block of code only when a given condition is True.

# AGE = int(input("Enter your age: "))

# if AGE >= 18:
#     print("you are aligible to vote ")

# NUM = eval(input("Enter a number: "))

# if NUM > 0:
#     print("The number is positive")

# num = (input("Enter a number: "))
# rev=num[::-1]
# if num==num[::-1]:
#     print("The number is a palindrome")

# 

svd = eval(input("Enter a data: "))
print(type(svd))
if type(svd) in (int, float, complex , bool):
    print("The data is a svd")
