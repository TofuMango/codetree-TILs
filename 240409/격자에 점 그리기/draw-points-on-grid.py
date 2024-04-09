n, m = tuple(map(int, input().split()))

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, m+1):
    r, c = list(map(int, input().split()))
    answer[r-1][c-1] = i

for row in range(n):
    for col in range(n):
        print(answer[row][col], end=" ")
    print()