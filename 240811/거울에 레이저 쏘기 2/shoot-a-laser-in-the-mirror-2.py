# 입력
n = int(input())
# 맵정보 입력
map = [
    input()
    for _ in range(n)
]
# 시작위치 입력
start_num = int(input())
# 맵 범위 정의
def in_range(x, y):
    return x>=0 and y>=0 and x<n and y<n
# 시작위치 구하는 함수정의
def primary(num):
    # 맵 위쪽에서 시작
    if num <= n:
        # x는 1행(보정- 0행) 고정이므로 0
        # 시작방향의 경우 0이 아래, 1이 왼쪽, 2가 위쪽, 3이 오른쪽
        return 0, num-1, 0
    # 맵 오른쪽에서 시작
    elif num <= 2 * n:
        # y는 n열고정이므로 n-1
        return num-n-1, n-1, 1
    # 맵 아래쪽에서 시작
    elif num <= 3 * n:
        # x는 n행 고정이므로 n-1
        return n-1, n-(num-2*n), 2
    else:
        # 맵 왼쪽에서 시작 y는 0행고정임
        return n-(num-3*n), 0, 3

# 다음 위치로 이동하기
def move(x,y,next_dir):
    # 아래 왼 위 오 순서
    dx, dy = [1,0,-1,0], [0,-1,0,1]
    nx, ny = x+dx[next_dir], y+dy[next_dir]
    return nx, ny, next_dir 

# 시뮬레이션 
def simulation(x,y,move_dir):
    # 이동횟수는 초기값은 0
    move_num = 0
    # 맵 밖을 벗어나면 종료
    while in_range(x,y):
        # (x,y) 위치의 거울이 /방향일때 처리
        if map[x][y] == "/":
            # 현재 방향에서 1 xor해주면 다음 위치 결정가능
            x, y, move_dir = move(x, y, move_dir ^ 1)
        # 거울이 \ 방향일때 처리
        else:
            x, y, move_dir = move(x, y, 3-move_dir)
        # 이동횟수 1증가
        move_num+=1
    return move_num

# 시작 위치 및 방향 구하기
x, y, move_dir = primary(start_num)
# 시작정보들 기반으로 시뮬레이션 돌리기
move_num = simulation(x,y, move_dir)
# 정답출력
print(move_num)