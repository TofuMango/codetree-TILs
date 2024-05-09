# # class 정의
# class Spot:
#     def __init__(self, index, x, y):
#         self.index, self.x, self.y = index, x, y
# # 점의 수 N
# n = int(input())
# # 점 객체 선언 후 입력받기
# spots = []
# for i in range(n):
#     x, y = tuple(map(int, input().split()))
#     spots.append((Spot(i+1, x, y)))
# # 원점
# x0, y0 = 0, 0
# # 거리가 가까운 점
# minX, minY = 1,001, 1,001
# # 원점과의 비교 후 출력하기
# for spot in spots:
#     if (x0 - spot.x) < minX and +(y0 - spot.y) < minY:
#         minX = spot.x
#         minY = spot.y
# class 정의
class Spot:
    def __init__(self, index, x, y):
        self.index, self.x, self.y = index, x, y

# 점의 수 N
n = int(input())
# 점 객체 선언 후 입력받기
spots = []
for i in range(n):
    x, y = map(int, input().split())  # tuple 불필요, 직접 unpacking
    spots.append(Spot(i+1, x, y))  # 괄호 수정

# 원점
x0, y0 = 0, 0
# 거리가 가까운 점 초기화
min_dist = float('inf')  # 최소 거리의 제곱을 저장할 변수
closest_spot = None  # 가장 가까운 점을 저장할 변수

# 원점과의 비교 후 가장 가까운 점 찾기
for spot in spots:
    dist_sq = (x0 - spot.x)**2 + (y0 - spot.y)**2  # 거리의 제곱 계산
    if dist_sq < min_dist:  # 현재 점이 더 가까우면 정보 갱신
        min_dist = dist_sq
        closest_spot = spot

# 가장 가까운 점의 index 출력
print(closest_spot.index)