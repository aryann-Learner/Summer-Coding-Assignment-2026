# Q32 - Print repeated-number pattern 1 22 333...
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(str(i) * i)