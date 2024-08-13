import sys

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

# 최소 거리 초기화
min_distance = sys.maxsize

# 각 방을 시작점으로 설정
for start in range(n):
    total_distance = 0
    # 각 방에 대해 거리 계산
    for j in range(n):
        # start 방에서 j 방까지의 거리
        distance = (j - start) % n  # 시계 반대 방향으로의 거리
        total_distance += arr[j] * distance  # 사람 수 * 거리

    # 최소 거리 갱신
    min_distance = min(min_distance, total_distance)

# 결과 출력
print(min_distance)