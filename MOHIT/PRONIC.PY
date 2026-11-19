num = int(input("Enter the number: "))

flag = False
i = 1

while i <= num//2:

    pro = i * (i+1)

    if pro == num:
        print(f"{num} is a Pronic number")
        flag = True
        break

    i += 1

if flag == False:
    print(f"{num} is not a Pronic number")