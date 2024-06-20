# n = int(input())
# res = [0] * 100
# for i in range(n):
#     a, b = tuple(map(int, input().split()))
#     if a <= 0:
#         a += abs(a)
#         b += abs(a)
#         for j in range(a-1,b-1):
#             res[j]+=1
#     for j in range(a-1,b-1):
#         res[j]+=1
# print(max(res))
n = int(input())
events = []

# 이벤트 리스트에 시작과 끝점을 기록
for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))  # 선분 시작
    events.append((b, -1))  # 선분 끝

# 이벤트를 정렬합니다. 시작점을 우선으로 정렬하고, 동일한 경우 끝점을 그 다음으로 정렬
events.sort()

max_overlap = 0
current_overlap = 0

# 이벤트를 순회하며 겹치는 선분 수를 계산
for x, event in events:
    current_overlap += event
    if current_overlap > max_overlap:
        max_overlap = current_overlap

print(max_overlap)