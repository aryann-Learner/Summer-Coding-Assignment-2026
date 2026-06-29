# Q39 - Print number pyramid 1 121 12321...
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print(' ' * (n - i) + ''.join(map(str, row)))