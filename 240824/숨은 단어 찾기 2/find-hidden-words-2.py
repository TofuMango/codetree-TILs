n, m = map(int, input().split())
arr = [
    input()
    for _ in range(n)
]

# dxs, dys 정의, 아래쪽 대각선을 기준으로 시계방향으로 정의
dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

# 격자 범위 정의
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

ans = 0
# 모든 좌표 하나씩 검사
for i in range(n):
    for j in range(m):
        # 만약 arr[i][j]값이 'L'이 아니면 다음 좌표로 이동
        if arr[i][j] != 'L':
            continue

        # 각 방향별로 검사해보기
        for dx, dy in zip(dxs, dys):
            # L을 포함하기때문에 1부터 시작
            cnt = 1  # cnt를 방향별로 초기화
            curx = i
            cury = j
            
            while True:
                nx = curx + dx
                ny = cury + dy
                
                # 범위 밖이면 반복문 탈출
                if in_range(nx, ny) == False:
                    break
                
                # arr[nx][ny]값이 'E'가 아닐경우 반복문 탈출
                if arr[nx][ny] != 'E':
                    break
                
                # 'e'라면
                cnt += 1
                curx = nx
                cury = ny
            
            # 'LEE가 완성된다면
            if cnt >= 3:
                ans += 1

print(ans)