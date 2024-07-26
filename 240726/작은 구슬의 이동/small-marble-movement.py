# <입력>
# n행/열, t초 
n, t = tuple(map(int, input().split()))
# 현재위치 (r행, c열), 방향 d
r, c, d = tuple(input().split())
r, c = int(r), int(c)
# 좌표평면 설정
arr = [0 for _ in range(n)]
# dx, dy 설정(우하상좌 순)
dx, dy = [0,1,-1,0], [1,0,0,-1]
# 매핑작업 수행
mapping = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}
d = mapping[d]
# 격자 범위 설정
def arr_range(x, y):
    return x<n and x>=0 and y<n and y>=0
# 구슬 이동시키기(t초가 0이 되면 빠져나옴)
while t >= 0:
    rx, cy = r + dx[d], c + dy[d]
    # 범위 벗어난경우 반대방향으로 전환
    if not arr_range(rx, cy):
        d = 3 - d
    # 구슬 움직이기
    r, c = r + dx[d], c + dy[d]
    print(r, c)
    t -= 1
print(r, c)