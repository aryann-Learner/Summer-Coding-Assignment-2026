# Q76 - Find diagonal sum
n = int(input("Size (nxn): "))
A = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(n)]
print(f"Diagonal sum = {sum(A[i][i] for i in range(n))}")