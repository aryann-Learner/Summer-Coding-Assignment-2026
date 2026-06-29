# Q97 - Merge two sorted arrays
arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))
print("Merged sorted:", sorted(arr1 + arr2))