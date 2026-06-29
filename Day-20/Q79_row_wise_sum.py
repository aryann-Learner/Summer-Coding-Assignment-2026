# Q79 - Find row-wise sum
r = int(input("Rows: "))
c = int(input("Cols: "))
A = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(r)]
for i, row in enumerate(A):
    print(f"Row {i+1} sum = {sum(row)}")