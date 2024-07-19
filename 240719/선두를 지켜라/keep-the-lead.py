# 명령 횟수 각각 입력
n, m = tuple(map(int, input().split()))
# a 시간별 이동거리 수를 저장할 배열
a_distance = [0] * 1000
b_distance = [0] * 1000
# 현재시간상태
a_time = 0
# 현재거리상태
a_now_dis = 0
# a 이동 명령 받는 배열
for _ in range(n):
    # 속력 및 시간 입력
    v, t = tuple(map(int,input().split()))
    # 시간 만큼 반복
    for i in range(t):
        a_now_dis += v
        # 현재 시간
        a_distance[a_time] += a_now_dis
        a_time += 1

# 현재시간상태
b_time = 0
# 현재거리상태
b_now_dis = 0
# B이동 명령 받는 배열
for _ in range(m):
    # 속력 및 시간 입력
    v, t = tuple(map(int,input().split()))
    # 시간 만큼 반복
    for i in range(t):
        b_now_dis += v
        # 현재 시간
        b_distance[b_time] += b_now_dis
        b_time += 1

ans = [0] * 1000
for i in range(a_time):
    if a_distance[i] > b_distance[i]:
        ans[i] = 'A'
    elif a_distance[i] == b_distance[i]:
        ans[i] = 'N'
    else:
        ans[i] = 'B'
cnt = 0
for i in range(a_time):
    if (ans[i] == 'A' and ans[i-1] =='B') or (ans[i] == 'B' and ans[i-1] =='A') or (ans[i] == 'A' and ans[i-1] =='N') or (ans[i] == 'B' and ans[i-1] =='N'):
        cnt += 1
print(cnt)