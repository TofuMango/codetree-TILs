# 입력
n, m = tuple(map(int, input().split()))
# 정답을 저장할 2차원배열 설정
ans = [
    [0] * m
    for _ in range(n)
]
# dx, dy 설정(우,하,좌,상 순)
dx, dy = [0,1,0,-1], [1,0,-1,0]
# 현재 방향 및 좌표 설정
x, y = 0,0
dir_num = 0
# 처음위치는 1시작
ans[x][y] = 1
# 범위설정
def arr_range(x, y):
    return x>=0 and y>=0 and x<n and y<m
# n*m번 진행. 1은있으니까 2부터~16까지
for i in range(2, n * m + 1):
    # 현재 기준 다음 위치값 계산
    nx, ny = x+dx[dir_num], y+dy[dir_num]
    # 범위 밖이거나 한번 지나갔던 곳일때 90도 회전
    if not arr_range(nx, ny) or ans[nx][ny] != 0:
        dir_num = (dir_num+1)%4
    # 좌표 이동시키고 값채워넣기
    x, y = x+dx[dir_num], y+dy[dir_num]
    ans[x][y] = i
    
# 출력
for row in range(n):
    for col in range(m):
        print(ans[row][col], end=' ')
    print()