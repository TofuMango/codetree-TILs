MAX_T = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매 초마다 서있는 위치를 기록
time_a = 1
# n = a의 이동명령횟수
for _ in range(n):
    # d는 방향 t는 초
    d, t = tuple(input().split())
    # 초만큼 반복
    for _ in range(int(t)):
        # a[현재시간] = a[현재시간-1](즉 이전시간)의 값에다가 d가 R이라면 +1더해주고, L이라면 -1
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        # 시간 1증가
        time_a += 1

# B가 매 초마다 서있는 위치를 기록
time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

# 최초로 만나는 시간
# -1은 둘이 만나지 않았을때 출력되어야하니까 -1로 초기화해줌
ans = -1
# time_a == time_b 걸린시간은 서로 동일함
for i in range(1, time_a):
    # 둘이 서로 같은시간에 같은값이 되는 순간 ans를 i 초로 저장
    if pos_a[i] == pos_b[i]:
        ans = i
        break
        
print(ans)