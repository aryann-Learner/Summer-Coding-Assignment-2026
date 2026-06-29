# Q63 - Find pair with given sum
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))
seen = set()
found = False
for x in arr:
    if target - x in seen:
        print(f"Pair found: ({target - x}, {x})")
        found = True
        break
    seen.add(x)
if not found:
    print("No pair found")