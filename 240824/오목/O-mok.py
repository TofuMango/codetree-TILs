import sys
# 입력
arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 범위 내인지 확인하는 함수
def in_range(x,y):
    return x>=0 and y>=0 and x<19 and y<19
# 왼쪽아래 대각선을 기준, 시계방향으로 정의
dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

# 전체 좌표를 다 확인해봄(0~18)
for i in range(19):
    for j in range(19):
        # 좌표값이 0일때
        if arr[i][j] == 0:
            continue
        for dx, dy in zip(dxs, dys):
            cnt = 1
            curx = i
            cury = j
            # 각 방향별로 카운팅해봄
            while True:
                nx = curx + dx
                ny = cury + dy
                # 좌표밖이면 while문 탈출
                if in_range(nx, ny) == False:
                    break
                # 돌색이 바뀌면 while문 탈출(한칸이동한 값과 현재값 다르면 break)
                if arr[nx][ny] != arr[i][j]:
                    break
                # 아니라면 카운팅 +1
                cnt += 1
                curx = nx
                cury = ny
                # 만약 오목이 완성되면 출력하고 프로그램 종료
            if cnt == 5:
                print(arr[i][j])
                print(i+2*dx+1, j+2*dy+1)
                sys.exit()
# 반복문 다돌때까지 승부안나면 0출력
print(0)