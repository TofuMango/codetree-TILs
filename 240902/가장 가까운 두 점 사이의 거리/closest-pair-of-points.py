import sys
n = int(input())
points = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = sys.maxsize
# 비교할 첫번째 점
for i, (x1, y1) in enumerate(points):
    dis = 0
    # 비교할 두번째 점
    for j, (x2, y2) in enumerate(points):
        # 만약에 같은점을 비교하게된다면 continue
        if i == j:
            continue
        # 서로 같은점이 아니라면
        x1, y1 = points[i]
        x2, y2 = points[j]
        # 제곱구하기
        # 두점사이가 가까울수록 제곱값이 작아질거니까...
        dis = abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2)
        ans = min(ans, dis)
print(ans)

# 답안
# import sys

# INT_MAX = sys.maxsize

# # 변수 선언 및 입력
# n = int(input())
# points = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]


# # 두 점 사이의 거리의 제곱 값을 반환합니다.
# def dist(i, j):
#     x1, y1 = points[i]
#     x2, y2 = points[j]
#     return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)


# # 모든 쌍에 대해서 거리 제곱값을 계산하여
# # 그 중 최솟값을 찾습니다.   
# min_dist = INT_MAX
# for i in range(n):
#     for j in range(i + 1, n):
#         min_dist = min(min_dist, dist(i, j))

# print(min_dist)