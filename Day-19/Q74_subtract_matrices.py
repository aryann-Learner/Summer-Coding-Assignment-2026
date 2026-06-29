# Q74 - Subtract matrices
r = int(input("Rows: "))
c = int(input("Cols: "))
A = [list(map(int, input(f"Row {i+1} of A: ").split())) for i in range(r)]
B = [list(map(int, input(f"Row {i+1} of B: ").split())) for i in range(r)]
result = [[A[i][j] - B[i][j] for j in range(c)] for i in range(r)]
print("Difference:", result)