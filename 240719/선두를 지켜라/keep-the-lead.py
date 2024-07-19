max_space = 1000000
# 명령 횟수 각각 입력
n, m = tuple(map(int, input().split()))
# a 시간별 이동거리 수를 저장할 배열
a_distance = [0] * max_space
b_distance = [0] * max_space
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
# 여기서 쉽게 쓰려면 now_dis 말고 현재시간 = 바로이전시간+v하면됨.
# 이때, time은 0초가아닌 1초시작으로 해야함. 

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

# ans = [0] * max_space
# for i in range(a_time):
#     if a_distance[i] > b_distance[i]:
#         ans[i] = 'A'
#     elif a_distance[i] == b_distance[i]:
#         ans[i] = 'N'
#     else:
#         ans[i] = 'B'
# cnt = 0
# for i in range(a_time):
#     if (ans[i] == 'A' and ans[i-1] =='B') or (ans[i] == 'B' and ans[i-1] =='A') or (ans[i] == 'A' and ans[i-1] =='N') or (ans[i] == 'B' and ans[i-1] =='N'):
#         cnt += 1
# print(cnt)

# 이부분 쉽게 하려면
# A와 B중 앞서있는 경우 파악하기
# a가 리더면 1, b가 리더면 2로 관리
leader, ans = 0, 0
for i in range(1, a_time):
    # 지금 a가 b를 앞설때
    if a_distance[i] > b_distance[i]:
        # 기존 리더가 b였다면
        # 답 갱신
        if leader == 2:
            ans += 1
        # 리더를 a로 변경
        leader = 1
    elif a_distance[i] < b_distance[i]:
        # 기존리더가 A였다면
        # 답 갱신하고 
        if leader == 1:
            ans += 1
        # 리더 b로 변경
        leader = 2
print(ans)