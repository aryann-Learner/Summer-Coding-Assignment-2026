# Q8 - Check whether a number is palindrome
def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

n = int(input("Enter number: "))
print("Palindrome" if is_palindrome(n) else "Not Palindrome")