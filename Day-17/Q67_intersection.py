# Q67 - Intersection of arrays
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
print("Intersection:", list(set(arr1) & set(arr2)))