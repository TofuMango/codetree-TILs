# # <입력>
# # n행/열, t초 
# n, t = tuple(map(int, input().split()))
# # 현재위치 (r행, c열), 방향 d
# r, c, d = tuple(input().split())
# r, c = int(r), int(c)
# # 좌표평면 설정
# arr = [0 for _ in range(n)]
# # dx, dy 설정
# dx, dy = [0,1,-1,0], [1,0,0,-1]
# # 매핑작업 수행
# mapping = {
#     'R' : 0,
#     'D' : 1,
#     'U' : 2,
#     'L' : 3
# }
# d = mapping[d]
# # 격자 범위 설정
# def arr_range(x, y):
#     return x<n and x>=0 and y<n and y>=0
# # 구슬 이동시키기(t초가 0이 되면 빠져나옴)
# for _ in range(t):
#     rx, cy = r + dx[d], c + dy[d]
#     # 범위 벗어난경우 반대방향으로 전환
#     if not arr_range(rx, cy):
#         d = 3 - d
#     # 구슬 움직이기
#     r, c = r + dx[d], c + dy[d]

# print(r, c)

def move_marbles(n, t, r, c, d):
    # 초기 방향 설정
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    # 방향 전환 설정
    reverse_direction = {
        'U': 'D',
        'D': 'U',
        'L': 'R',
        'R': 'L'
    }
    
    # 초기 방향 설정
    dr, dc = directions[d]
    
    for _ in range(t):
        # 다음 위치 계산
        nr = r + dr
        nc = c + dc
        
        # 벽에 부딪히는지 확인
        if nr < 1 or nr > n:
            # 행 방향으로 벽에 부딪히면
            dr = -dr
        if nc < 1 or nc > n:
            # 열 방향으로 벽에 부딪히면
            dc = -dc
        
        # 벽에 부딪혔을 때 방향만 바꾸고 위치는 업데이트하지 않음
        if nr < 1 or nr > n or nc < 1 or nc > n:
            continue
        
        # 위치 업데이트
        r = nr
        c = nc
    
    return r, c

# 입력 받기
n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)

# 방향 설정
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
reverse_direction = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}
dr, dc = directions[d]

# 결과 계산
result_r, result_c = move_marbles(n, t, r, c, d)

# 결과 출력
print(result_r, result_c)