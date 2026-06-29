# Q85 - Check palindrome string
s = input("Enter string: ").lower().replace(" ", "")
print("Palindrome" if s == s[::-1] else "Not Palindrome")