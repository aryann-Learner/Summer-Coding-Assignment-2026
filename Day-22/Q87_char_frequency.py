# Q87 - Character frequency
s = input("Enter string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print("Frequency:", freq)