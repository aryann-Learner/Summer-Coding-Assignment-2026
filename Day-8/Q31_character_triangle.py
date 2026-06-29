# Q31 - Print character triangle A AB ABC...
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(''.join(chr(65 + j) for j in range(i)))