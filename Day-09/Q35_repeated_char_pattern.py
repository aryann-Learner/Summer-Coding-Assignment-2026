# Q35 - Print repeated character pattern A BB CCC...
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(chr(64 + i) * i)