# Q55 - Second largest element
arr = list(map(int, input("Enter elements: ").split()))
unique = sorted(set(arr))
print(f"Second largest = {unique[-2]}" if len(unique) >= 2 else "Not enough elements")