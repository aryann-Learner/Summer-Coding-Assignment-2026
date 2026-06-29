# Q53 - Linear search
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key to search: "))
found = -1
for i, val in enumerate(arr):
    if val == key:
        found = i
        break
print(f"Found at index {found}" if found != -1 else "Not found")