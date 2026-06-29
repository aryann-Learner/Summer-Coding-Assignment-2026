# Q40 - Print character pyramid A ABA ABCBA...
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    chars = [chr(64 + j) for j in range(1, i + 1)]
    row = chars + chars[-2::-1]
    print(' ' * (n - i) + ''.join(row))