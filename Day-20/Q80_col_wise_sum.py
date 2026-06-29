# Q80 - Find column-wise sum
r = int(input("Rows: "))
c = int(input("Cols: "))
A = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(r)]
for j in range(c):
    print(f"Col {j+1} sum = {sum(A[i][j] for i in range(r))}")