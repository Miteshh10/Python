# i = 1
# count = 0

# while count < 20:
#     if i % 2 == 0:
#         print(i)
#         count += 1

#     i += 1


# i = 3

# while i <= 50:
#     print(i)
#     i += 3

i = 1

while i <= 50:

    if i % 3 == 0 and i % 5 == 0:
        print(i)

    i += 1


i = 1
total = 0

while i <= 10:
    total = total + i
    i += 1

print("Sum:", total)

num = 12345
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total digits:", count)