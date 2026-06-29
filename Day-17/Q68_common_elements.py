# Q68 - Find common elements
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
print("Common elements:", [x for x in arr1 if x in arr2])