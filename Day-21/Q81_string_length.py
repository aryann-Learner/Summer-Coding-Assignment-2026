# Q81 - Find string length without len()
s = input("Enter string: ")
count = 0
for _ in s:
    count += 1
print(f"Length = {count}")