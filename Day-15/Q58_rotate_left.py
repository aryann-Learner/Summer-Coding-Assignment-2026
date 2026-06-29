# Q58 - Rotate array left
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter positions to rotate left: "))
k = k % len(arr)
print("Rotated left:", arr[k:] + arr[:k])