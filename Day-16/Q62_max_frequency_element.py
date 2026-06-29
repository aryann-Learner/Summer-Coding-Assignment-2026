# Q62 - Find maximum frequency element
from collections import Counter
arr = list(map(int, input("Enter elements: ").split()))
c = Counter(arr)
print(f"Max frequency element = {c.most_common(1)[0][0]}")