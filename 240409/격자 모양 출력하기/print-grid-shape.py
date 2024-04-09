n, m = tuple(map(int, input().split()))
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r, c = list(map(int, input().split()))
    answer[r-1][c-1] =  r * c

for row in range(n):
    for col in range(n):
        print(answer[row][col], end=" ")
    print()