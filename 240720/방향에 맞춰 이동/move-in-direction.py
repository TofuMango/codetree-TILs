N = int(input())
x, y = 0, 0
# 동서남북 정보입력
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

for _ in range(N):
    d, v = tuple(input().split())
    if d == 'W':
        d = 0
    elif d == 'S':
        d = 1
    elif d == 'N':
        d = 2
    else:
        d = 3
    for _ in range(int(v)):
        x, y = x + dx[d], y + dy[d]
print(abs(x), abs(y))