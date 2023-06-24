

user = int(input("enter a positive number greater than 1"))

for num in range(2, user + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
