max_xy = 40000
n = int(input())
spots = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = max_xy
# 제외할 점위치 정함
for i in range(n):
    # i번 점 제외하고 나머지 점 포함해야함
    # 최소 넓이 : 남은 점들의 x좌표중 최소, 최대 / y좌표중 최소, 최대
    # 최소값을 구하려면 일단 제일 큰수로 초기화, 최대값 구하려면 작은 수로 초기화
    min_x, max_x = max_xy, 1
    min_y, max_y = max_xy, 1
    # j는 인덱스값이고,, (x,y)는 spots에 저장된 점 위치 좌표정보들
    for j, (x, y) in enumerate(spots):
        # i번째 점은 제외함
        if j == i:
            continue
        # 현재 x와 미리 초기화해놨던 변수랑 비교하기
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    # 가능한 직사각형 넓이 중 최소값을 ans에 저장
    ans = min(ans, (max_x - min_x) * (max_y - min_y))
print(ans)