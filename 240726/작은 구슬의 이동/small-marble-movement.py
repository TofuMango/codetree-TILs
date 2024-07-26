# <입력>
# n행/열, t초 
n, t = tuple(map(int, input().split()))
# 현재위치 (r행, c열), 방향 d
r, c, d = tuple(input().split())
r, c = int(r), int(c)
# 좌표평면 설정
arr = [0 for _ in range(n)]
# dx, dy 설정
dx, dy = [0,1,-1,0], [1,0,0,-1]
# 매핑작업 수행
mapping = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}
d = mapping[d]
# 현재 좌표값 보정. 1행 시작이 아닌 0행 시작이기때문
r, c = r-1, c-1
# 격자 범위 설정
def arr_range(x, y):
    return x<n and x>=0 and y<n and y>=0
# 구슬 이동시키기(t초가 0이 되면 빠져나옴)
for _ in range(t):
    rx, cy = r + dx[d], c + dy[d]
    # 범위 벗어난경우 반대방향으로 전환
    if not arr_range(rx, cy):
        d = 3 - d
    else:
        # 벗어나지 않았다면 그대로 실행
        r, c = r + dx[d], c + dy[d]

# 좌표값 보정해서 출력하기
print(r+1, c+1)