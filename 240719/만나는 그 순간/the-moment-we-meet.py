n, m = map(int, input().split())

# A와 B의 이동 경로를 저장할 리스트
dirA = [tuple(input().split()) for _ in range(n)]
dirB = [tuple(input().split()) for _ in range(m)]

# 이동 경로를 기록할 딕셔너리
positionsA = {}
positionsB = {}

# 현재 위치를 저장할 변수
posA = 0
posB = 0

# 시간 기록용 변수
timeA = 0
timeB = 0

# A의 이동 경로 기록
for direction, num in dirA:
    num = int(num)
    for _ in range(num):
        if direction == 'R':
            posA += 1
        elif direction == 'L':
            posA -= 1
        timeA += 1
        positionsA[timeA] = posA

# B의 이동 경로 기록
for direction, num in dirB:
    num = int(num)
    for _ in range(num):
        if direction == 'R':
            posB += 1
        elif direction == 'L':
            posB -= 1
        timeB += 1
        positionsB[timeB] = posB

# 최초로 만나는 시간을 찾기
meeting_time = -1
for t in range(1, max(timeA, timeB) + 1):
    if positionsA.get(t) == positionsB.get(t):
        meeting_time = t
        break

print(meeting_time)