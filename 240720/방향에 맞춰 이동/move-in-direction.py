N = int(input())
x, y = 0, 0

# 동서남북 방향 정의
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(N):
    d, v = input().split()
    v = int(v)
    
    if d == 'E':
        dir_num = 0
    elif d == 'W':
        dir_num = 1
    elif d == 'N':
        dir_num = 2
    elif d == 'S':
        dir_num = 3
    
    x, y = x + dx[dir_num] * v, y + dy[dir_num] * v

print(x, y)