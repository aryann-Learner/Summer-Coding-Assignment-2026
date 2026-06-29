# Q92 - Find maximum occurring character
s = input("Enter string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(f"Max occurring char = {max(freq, key=freq.get)}")