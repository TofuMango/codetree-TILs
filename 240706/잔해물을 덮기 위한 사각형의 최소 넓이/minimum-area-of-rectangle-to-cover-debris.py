offset = 1000
maxSpace = offset * 2
square = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

# 좌표 변환
transformed_squares = []
for (x1, y1, x2, y2) in square:
    x1, y1 = offset + x1, offset + y1
    x2, y2 = offset + x2, offset + y2
    transformed_squares.append((x1, y1, x2, y2))

# 교차 영역 계산
def calculate_intersection_area(sq1, sq2):
    x1 = max(sq1[0], sq2[0])
    y1 = max(sq1[1], sq2[1])
    x2 = min(sq1[2], sq2[2])
    y2 = min(sq1[3], sq2[3])

    if x1 < x2 and y1 < y2:
        return (x2 - x1) * (y2 - y1)
    else:
        return 0

area = calculate_intersection_area(transformed_squares[0], transformed_squares[1])
print(area)