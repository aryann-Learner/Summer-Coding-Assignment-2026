# Q98 - Find common characters in strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Common characters:", list(set(s1) & set(s2)))