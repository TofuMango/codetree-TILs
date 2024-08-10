# 입력
n, m = tuple(map(int, input().split()))
# 격자 만들기
arr = [ [0] * n for _ in range(n)]
# dx, dy 정의(상,좌,하,우)순
dxs, dys = [-1,0,1,0],[0,1,0,-1]
dir_num = 0
# 배열 범위 설정
def arr_range(x, y):
    return x>=0 and y>=0 and x<n and y<n
# 명령 갯수만큼 반복 실행
for _ in range(m):
    # r = x, c = y 좌표
    r, c = tuple(map(int, input().split()))
    # 좌표값 보정
    r -= 1
    c -= 1
    # 입력받은 좌표가 색칠되지 않았으면 색칠
    if arr[r][c] != 1:
        arr[r][c] = 1
    # 만약 입력받은 좌표의 상, 하, 좌, 우 중 3칸이 1이라면 1출력
    tmp = 0
    for i in range(4):
        dx, dy = r + dxs[i], c + dys[i]
        if arr_range(dx, dy) and arr[dx][dy] == 1 and tmp < 4:
            tmp += 1
    if tmp == 3:
        print(1)
    else:
        print(0)