# Q64 - Remove duplicates from array
arr = list(map(int, input("Enter elements: ").split()))
print("Without duplicates:", list(dict.fromkeys(arr)))