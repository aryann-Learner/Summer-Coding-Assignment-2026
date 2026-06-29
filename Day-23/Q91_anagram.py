# Q91 - Check anagram strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if sorted(s1.lower()) == sorted(s2.lower()) else "Not Anagram")