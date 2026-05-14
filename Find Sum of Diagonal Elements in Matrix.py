n = int(input("Enter size of matrix: "))
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary = sum(matrix[i][i] for i in range(n))
secondary = sum(matrix[i][n-i-1] for i in range(n))

print("Diagonal sum:", primary + secondary)