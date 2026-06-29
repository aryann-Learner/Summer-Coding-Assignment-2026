# Q100 - Sort words by length
s = input("Enter sentence: ")
print("Sorted by length:", sorted(s.split(), key=len))