# Q96 - Remove duplicate characters
s = input("Enter string: ")
seen = set()
result = ""
for c in s:
    if c not in seen:
        result += c
        seen.add(c)
print(f"Without duplicates = {result}")