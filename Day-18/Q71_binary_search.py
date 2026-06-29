# Q71 - Binary search
arr = sorted(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))
low, high = 0, len(arr) - 1
found = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
print(f"Found at index {found}" if found != -1 else "Not found")