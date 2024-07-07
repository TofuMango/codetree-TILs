# 사각형 갯수 입력
n = int(input())
# 음수 보정
offset = 100
# 최댓값 설정
maxSpace = offset * 2
# 사각형 좌표정보 입력받기
square = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
# 색깔정보 저장
check = [
    [0] * (maxSpace + 1)
    for _ in range(maxSpace + 1)
]

for index, (x1, y1, x2, y2) in enumerate(square, start = 1):
    # offset 적용
    x1, y1 = offset+x1, offset+y1
    x2, y2 = offset+x2, offset+y2

    for i in range(x1, x2):
        for j in range(y1, y2):
            # 짝수일때 파란색(2)를 저장
            if index % 2 == 0:
                check[i][j] = 2
            # 홀수일때 빨간색(1)
            else:
                check[i][j] = 1
cnt = 0
# 파란색 영역 넓이만 출력
for row in range(maxSpace+1):
    for col in range(maxSpace+1):
        if check[row][col] == 2:
            cnt += 1
print(cnt)