# Q33 - Print reverse star pattern
n = int(input("Enter rows: "))
for i in range(n, 0, -1):
    print('*' * i)