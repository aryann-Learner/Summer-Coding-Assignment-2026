# Q52 - Count even and odd elements
arr = list(map(int, input("Enter elements: ").split()))
even = sum(1 for x in arr if x % 2 == 0)
odd = len(arr) - even
print(f"Even count = {even}, Odd count = {odd}")