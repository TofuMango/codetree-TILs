max_space = 1000000
# a이동횟수 n, b이동횟수 m 입력받기
n, m = tuple(map(int, input().split()))
# A와 B 이동거리 저장할 배열 0으로 초기화
pos_A, pos_B = [0] * (max_space + 1), [0] * (max_space + 1)

# A의 현재시간
A_time = 1
# A 이동거리 계산
for _ in range(n):
    t, d = input().split()
    for i in range(int(t)):
        if d == 'R':
            pos_A[A_time] = pos_A[A_time - 1] + 1
        else:
            pos_A[A_time] = pos_A[A_time - 1] - 1
        A_time += 1

# B 이동거리
B_time = 1
for _ in range(m):
    t, d = input().split()
    for i in range(int(t)):
        if d == 'R':
            pos_B[B_time] = pos_B[B_time - 1] + 1
        else:
            pos_B[B_time] = pos_B[B_time - 1] - 1
        B_time += 1

# A, B중 최대시간에 맞춰서 배열의 남은공간에 마지막 값 채워주기
maxtime = max(A_time, B_time)
if A_time > B_time:
    for i in range(B_time, maxtime):
        pos_B[i] = pos_B[i - 1]
else:
    for i in range(A_time, maxtime):
        pos_A[i] = pos_A[i - 1]

ans = 0
for i in range(1, maxtime):
    # 현재시간의 이동거리가 일치하면서, 이전시간의 거리는 일치하지 않을 때만 +1
    if pos_A[i] == pos_B[i] and pos_A[i - 1] != pos_B[i - 1]:
        ans += 1

print(ans)