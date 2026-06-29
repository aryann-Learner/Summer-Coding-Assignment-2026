# Q94 - Compress a string (run-length encoding)
s = input("Enter string: ")
result = ""
i = 0
while i < len(s):
    count = 1
    while i + count < len(s) and s[i + count] == s[i]:
        count += 1
    result += s[i] + (str(count) if count > 1 else "")
    i += count
print(f"Compressed = {result}")