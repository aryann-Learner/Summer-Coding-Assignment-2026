# Q75 - Transpose matrix
r = int(input("Rows: "))
c = int(input("Cols: "))
A = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(r)]
transpose = [[A[j][i] for j in range(r)] for i in range(c)]
print("Transpose:", transpose)