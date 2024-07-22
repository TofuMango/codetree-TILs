n = int(input())
# 좌표평면 입력
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
# dxs, dxy 정의(북동남서 순)
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 좌표 벗어나지않도록 함수 정의
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

tmp = 0
cnt = 0
for i in range(n):
    for j in range(n):
        x, y = i, j
        tmp = 0
        # 배열 두개 묶음으로 가져다 쓸때 zip 사용
        for dx, dy in zip(dxs, dys):
            # 현재 좌표에 dx, dy 더해주기
            nx, ny = x + dx, y + dy
            # 좌표평면을 벗어나지 않으면서 현재 좌표 주변에 1이 있다면 tmp += 1
            if in_range(nx, ny) and arr[nx][ny] == 1:
                tmp += 1
        # tmp가 3이상일때 cnt += 1하고 tmp 초기화
        if tmp >= 3:
            cnt += 1
print(cnt)