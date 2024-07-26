# 명령 횟수 입력
n = int(input())

# dx, dy 정의 (서, 남, 북, 동 순)
dx, dy = [0, 1, -1, 0], [-1, 0, 0, 1]

# 방향 매핑 정의
mapping = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}

# 시작 좌표
x, y = 0, 0

# 수행 시간
t = 0
check = False

for _ in range(n):
    d, s = tuple(input().split())
    s = int(s)
    d = mapping[d]
    for _ in range(s):
        x += dx[d], y += dy[d]
        t += 1  # t 증가
        if x == 0 and y == 0 and not check:
            check = True
            print(t)

if not check:
    print(-1)