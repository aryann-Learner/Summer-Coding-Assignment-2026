# Q61 - Find missing number in array (1 to n)
arr = list(map(int, input("Enter elements (1 to n with one missing): ").split()))
n = len(arr) + 1
print(f"Missing number = {n * (n + 1) // 2 - sum(arr)}")