# 2차원 배열 만들기
arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

# 합계 변수 초기화
sum = 0
# 색칠된 칸에 해당하는 정수를 고름
for i in range(4):
    for j in range(i+1):
        sum += arr_2d[i][j]
print(sum)