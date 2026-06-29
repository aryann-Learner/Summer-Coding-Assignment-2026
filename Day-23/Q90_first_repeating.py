# Q90 - Find first repeating character
s = input("Enter string: ")
seen = set()
result = None
for c in s:
    if c in seen:
        result = c
        break
    seen.add(c)
print(f"First repeating = {result}" if result else "No repeating character")