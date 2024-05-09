# class 정의
class Spot:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.manhattan_distance = abs(x) + abs(y)  # 멘하탄 거리 계산 및 저장

# 점의 수 N
n = int(input())
# 점 객체 선언 후 입력받기
spots = []
for i in range(n):
    x, y = map(int, input().split())
    spots.append(Spot(i+1, x, y))

# 멘하탄 거리와 인덱스를 기준으로 정렬
# 멘하탄 거리가 같은 경우, 점의 인덱스가 작은 순으로 정렬됨
spots.sort(key=lambda spot: (spot.manhattan_distance, spot.index))

# 정렬된 순서대로 점의 번호 출력
for spot in spots:
    print(spot.index)