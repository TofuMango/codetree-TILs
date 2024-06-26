n = int(input())
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    answer[i][0] = 1
    answer[0][i] = 1

for row in range(1,n):
    for col in range(1,n):
        answer[row][col] = answer[row-1][col-1] + answer[row-1][col] + answer[row][col-1]

for row in answer:
    for col in row:
        print(col, end=" ")
    print()