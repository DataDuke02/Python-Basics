rows = 2
cols = 2

print("Enter Matrix A :")
A = [[int(input()) for _ in range(cols)] for _ in range(rows)]

print("Enter Matrix B :")
B = [[int(input())for _ in range(cols)] for _ in range(rows)]

result = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] = A[i][j] + B[i][j]

print("Result : ")
for row in result:
    print(row)
