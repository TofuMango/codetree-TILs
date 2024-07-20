commands = input().strip()

# 방향을 북, 동, 남, 서로 정의
# 북쪽: (0, 1), 동쪽: (1, 0), 남쪽: (0, -1), 서쪽: (-1, 0)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 처음 좌표
x, y = 0, 0
# 처음 방향 (0: 북, 1: 동, 2: 남, 3: 서)
direction = 0

for command in commands:
    if command == 'L':
        direction = (direction - 1 + 4) % 4  # 왼쪽으로 90도 회전
    elif command == 'R':
        direction = (direction + 1) % 4  # 오른쪽으로 90도 회전
    elif command == 'F':
        x += dx[direction]
        y += dy[direction]

print(x, y)