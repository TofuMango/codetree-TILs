# # n = 5
# # segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]
# # ans = 100
# # # 제외할 선분 i
# # for i in range(n):
# #     # 선분 범위?
# #     # i번째 선분 빠질때마다 새로 계산되어야함
# #     count = [0] * 11
# #     for j in range(n):
# #         # 현재 선분과 제외할 선분이 같으면 넘어감
# #         if j == i:
# #             continue
# #         # 시작점, 끝점
# #         x1, x2 = segments[j]
# #         # 제외한 선분 제외한 나머지 선분 순회
# #         # x1이 2고 x2+1이 5면 2,3,4
# #         for k in range(x1, x2+1):
# #             count[k] += 1
# #     # 겹치는 최대갯수 카운팅
# #     max_cnt = max(count)
# #     ans = max(ans, max_cnt)
# # print(ans)
# max_xy = 40000
# n = int(input())
# spots = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]
# # 제외할 좌표값
# for i in range(n):
#     # 이거 해야하나 ??
#     # x중 최소값이랑, y중 최대값 고를거임
#     check_x = [0] * (max_xy+1)
#     check_y = [0] * (max_xy+1)

#     for j in range(n):
#         if i == j:
#             continue
#         # 만약 이러면 0번 정보 제외하고 (1,1)이 x랑 y로 선택될건데...
#         x, y = spots[j]
#         for k in range(x, ):
#             check_x[x] = 

def min_area_excluding_one_point(points):
    n = len(points)
    min_area = float('inf')  # 최소 넓이를 무한대로 초기화

    for i in range(n):
        # 현재 점을 제외한 나머지 점들
        remaining_points = points[:i] + points[i+1:]

        # 남은 점들의 x, y 좌표의 min, max 계산
        x_coords = [point[0] for point in remaining_points]
        y_coords = [point[1] for point in remaining_points]

        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords)
        y_max = max(y_coords)

        # 넓이 계산
        if x_min == x_max or y_min == y_max:  # 같은 x 또는 y일 경우 넓이는 0
            area = 0
        else:
            area = (x_max - x_min) * (y_max - y_min)

        # 최소 넓이 업데이트
        min_area = min(min_area, area)

    return min_area

# 입력 처리
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = min_area_excluding_one_point(points)
print(result)