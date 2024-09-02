n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 - x2) * (y3 - y1))//2

max_area = 0

# 모든 점의 조합을 확인
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            # (x1, y1)와 (x2, y2)로 x축에 평행한 변을 만든 경우
            if y1 == y2:  # x축에 평행한 변
                if y3 != y1:  # y축에 평행한 변을 만들 수 있는지 확인
                    area = calculate_area(x1, y1, x2, y2, x3, y3)
                    max_area = max(max_area, area)

            # (x2, y2)와 (x3, y3)로 x축에 평행한 변을 만든 경우
            if y2 == y3:  # x축에 평행한 변
                if y1 != y2:  # y축에 평행한 변을 만들 수 있는지 확인
                    area = calculate_area(x1, y1, x2, y2, x3, y3)
                    max_area = max(max_area, area)

            # (x1, y1)와 (x3, y3)로 x축에 평행한 변을 만든 경우
            if y1 == y3:  # x축에 평행한 변
                if y2 != y1:  # y축에 평행한 변을 만들 수 있는지 확인
                    area = calculate_area(x1, y1, x2, y2, x3, y3)
                    max_area = max(max_area, area)

# 결과 출력
print(max_area * 2)  # 넓이에 2를 곱해서 출력