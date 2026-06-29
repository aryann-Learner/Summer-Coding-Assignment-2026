# Q56 - Find duplicates in array
arr = list(map(int, input("Enter elements: ").split()))
seen = set()
duplicates = set()
for x in arr:
    if x in seen:
        duplicates.add(x)
    seen.add(x)
print(f"Duplicates = {list(duplicates)}")