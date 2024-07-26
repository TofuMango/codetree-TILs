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
num = 1
ans[0][0] = num
# 범위설정
def arr_range(x, y):
    return x>=0 and y>=0 and x<n and y<n
# 숫자세기
while True:
    nx, ny = x+dx[dir_num], y+dy[dir_num]
    # 범위 밖이거나 한번 지나갔던 곳일때
    if not arr_range(nx, ny) or ans[nx][ny] != 0:
        dir_num = (dir_num+1)%4
    else:
        # 좌표 이동시키기
        x, y = x+dx[dir_num], y+dy[dir_num]
        # 번호를 1증가시키고
        num += 1
        # ans 배열에 저장
        ans[x][y] = num
    # 숫자가 좌표평면 수와 일치하면 반복문 빠져나옴
    if num == n*m:
        break
# 출력
for row in range(n):
    for col in range(m):
        print(ans[row][col], end=' ')
    print()