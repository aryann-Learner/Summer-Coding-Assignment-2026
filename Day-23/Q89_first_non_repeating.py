# Q89 - Find first non-repeating character
from collections import Counter
s = input("Enter string: ")
freq = Counter(s)
result = next((c for c in s if freq[c] == 1), None)
print(f"First non-repeating = {result}" if result else "All characters repeat")