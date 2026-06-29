# Q60 - Move zeroes to end
arr = list(map(int, input("Enter elements: ").split()))
non_zero = [x for x in arr if x != 0]
result = non_zero + [0] * (len(arr) - len(non_zero))
print("After moving zeroes:", result)