# Q95 - Find longest word
s = input("Enter sentence: ")
print(f"Longest word = {max(s.split(), key=len)}")