matrix = [["●"] * 4 for _ in range(4)]
for i in range(4):
    matrix[i][i] = "○"

for row in matrix:
    print(" ".join(row))
