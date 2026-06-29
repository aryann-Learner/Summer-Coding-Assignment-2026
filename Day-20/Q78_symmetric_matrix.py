# Q78 - Check symmetric matrix
n = int(input("Size (nxn): "))
A = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(n)]
transpose = [[A[j][i] for j in range(n)] for i in range(n)]
print("Symmetric" if A == transpose else "Not Symmetric")