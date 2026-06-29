# Q66 - Union of arrays
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
print("Union:", list(set(arr1) | set(arr2)))