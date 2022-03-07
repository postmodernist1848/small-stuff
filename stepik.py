n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = i + j + 1

for row in matrix:
    for el in row:
        print(str(el).ljust(3), end = ' ')
    print()
    