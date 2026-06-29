# Q59 - Rotate array right
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter positions to rotate right: "))
k = k % len(arr)
print("Rotated right:", arr[-k:] + arr[:-k])