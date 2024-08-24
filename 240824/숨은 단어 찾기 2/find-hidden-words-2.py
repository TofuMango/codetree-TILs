n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

# 모든 방향: 오른쪽, 왼쪽, 아래쪽, 위쪽, 오른쪽 아래, 오른쪽 위, 왼쪽 아래, 왼쪽 위
dxs = [1, -1, 0, 0, 1, 1, -1, -1]  # x 방향
dys = [0, 0, 1, -1, 1, -1, 1, -1]  # y 방향

# 격자 범위 정의
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

ans = 0

# 모든 좌표 하나씩 검사
for i in range(n):
    for j in range(m):
        # 현재 위치에서 'L'로 시작하는 경우만 체크
        if arr[i][j] == 'L':
            # 각 방향별로 검사
            for d in range(8):  # 8 방향
                cnt = 0
                curx, cury = i, j
                
                # 'LEE'를 찾기 위해 2번 이동
                for k in range(3):  # 'L', 'E', 'E'를 찾기 위해 3번
                    if in_range(curx, cury) and arr[curx][cury] == 'LEE'[k]:
                        cnt += 1
                    else:
                        break
                    curx += dxs[d]
                    cury += dys[d]

                # 'LEE'를 찾은 경우
                if cnt == 3:  # 'LEE'를 찾았으면
                    ans += 1

# 출력
print(ans)

# n, m = map(int, input().split())
# arr = [
#     list(input())
#     for _ in range(n)
# ]

# # dxs, dys 정의, 아래쪽 대각선을 기준으로 시계방향으로 정의
# dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

# # 격자 범위 정의
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# ans = 0

# # 모든 좌표 하나씩 검사
# for i in range(n):
#     for j in range(m):
#         # 만약 arr[i][j]값이 'L'이 아니면 다음 좌표로 이동
#         if arr[i][j] != 'L':
#             continue

#         # 각 방향별로 검사해보기
#         for dx, dy in zip(dxs, dys):
#             cnt = 0  # cnt를 방향별로 초기화
#             curx = i
#             cury = j
            
#             while True:
#                 nx = curx + dx
#                 ny = cury + dy
                
#                 # 범위 밖이면 반복문 탈출
#                 if not in_range(nx, ny):
#                     break
                
#                 # arr[nx][ny]값이 'E'가 아닐경우 반복문 탈출
#                 if arr[nx][ny] != 'E':
#                     break
                
#                 # 'e'라면
#                 cnt += 1
#                 curx = nx
#                 cury = ny
            
#             # 'e'가 두 개 이상 나온 경우
#             if cnt == 2:
#                 ans += 1

# print(ans)