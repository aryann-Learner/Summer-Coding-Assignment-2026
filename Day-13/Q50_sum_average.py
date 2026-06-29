# Q50 - Find sum and average of array
arr = list(map(int, input("Enter elements: ").split()))
total = sum(arr)
avg = total / len(arr)
print(f"Sum = {total}, Average = {avg:.2f}")