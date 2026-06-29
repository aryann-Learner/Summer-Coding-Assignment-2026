# Q99 - Sort names alphabetically
n = int(input("How many names? "))
names = [input(f"Name {i+1}: ") for i in range(n)]
print("Sorted names:", sorted(names))