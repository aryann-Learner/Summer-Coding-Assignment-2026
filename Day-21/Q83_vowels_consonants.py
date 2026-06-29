# Q83 - Count vowels and consonants
s = input("Enter string: ")
vowels = sum(1 for c in s.lower() if c in 'aeiou')
consonants = sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')
print(f"Vowels = {vowels}, Consonants = {consonants}")