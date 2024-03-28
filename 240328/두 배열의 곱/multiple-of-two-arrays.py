# 배열 2개 받아서 바로 처리하는 방법
# arr_2d_1 = [
#     list(map(int, input().split()))
#     for _ in range(3)
# ]
# # 줄 간격
# empty = input()

# arr_2d_2=[
#     list(map(int, input().split()))
#         for _ in range(3)
# ]
# result = 0

# for i in range(3):
#     for j in range(3):
#         result = (arr_2d_1[i][j]) * (arr_2d_2[i][j])
#         print(result, end=" ")
#     print()

# 별도의 배열을 만들어 결과를 담아 출력하는 방법
# 배열1
arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
# 공백
input()
# 배열2
arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]
# 배열3(결과값 담을 빈 배열)
arr_2d_3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

# 연산결과를 배열 3에 담음
for i in range(3):
    for j in range(3):
        arr_2d_3[i][j] = arr_2d_1[i][j] * arr_2d_2[i][j]

# 배열 3의 요소들 출력
# [2, 6, 12], [20, 30, 42] ...
for row in arr_2d_3:
    # 2, 6, 12 / 20, 30, 42 ...
    for col in row:
        print(col, end=" ")
    print()