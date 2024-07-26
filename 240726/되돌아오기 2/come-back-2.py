# 명령 입력받기
cmd = list(input())
# dx, dy 정의(북, 동, 남, 서 순)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# 현재 방향 및 위치 정의
x, y = 0, 0
d = 0
# 걸린 시간, 정답
elapsed_time = 0
ans = -1

for i in range(len(cmd)):
    elapsed_time += 1
    if cmd[i] == 'F':
        x, y = x + dx[d], y + dy[d]
    elif cmd[i] == 'L':
        d = (d - 1 + 4) % 4
    elif cmd[i] == 'R':
        d = (d + 1) % 4
    
    # 원점에 도달하는지 확인
    if x == 0 and y == 0:
        ans = elapsed_time
        break

print(ans)