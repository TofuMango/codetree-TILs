# 최대시간 설정
max_T = 1000000
# 입력
N, M = tuple(map(int, input().split()))
posA, posB = [0] * (max_T + 1), [0] * (max_T + 1)

# A 이동정보 입력
timeA = 1
for i in range(N):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        posA[timeA] = posA[timeA - 1] + v
        timeA += 1
# B 이동정보 입력
timeB = 1
for i in range(M):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        posB[timeB] = posB[timeB - 1] + v
        timeB += 1

win = [0] * (timeA)
for i in range(1, timeA):
    # 만약 A와 B를 비교해서 A가 더 빨랐다면
    if posA[i] > posB[i]:
        win[i] = 'A'
    elif posA[i] == posB[i]:
        win[i] = 'N'
    else:
        win[i] = 'B'

# 명예의전당 변경횟수 카운팅
cnt = 0
for i in range(1, timeA):
    if win[i] != win[i-1]:
        cnt += 1
print(cnt)