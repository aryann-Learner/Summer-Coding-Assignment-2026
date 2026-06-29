# Q77 - Multiply matrices
n = int(input("Size (nxn): "))
A = [list(map(int, input(f"Row {i+1} of A: ").split())) for i in range(n)]
B = [list(map(int, input(f"Row {i+1} of B: ").split())) for i in range(n)]
result = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
print("Product:", result)