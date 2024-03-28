# 0으로 채워져 있는 배열 만들기
# n = 4
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# print(arr_2d)

#n*m 사이즈의 격자
# n, m = 4,5
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# print(arr_2d)

# 2차원 배열 출력
# n = 4
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# for i in range(n):
#     for j in range(n):
#         print(arr_2d[i][j], end=" ")
#     print()

# 리스트 내 원소 바로 접근
# n = 4
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# # ex) arr_2d 내부의 [1,2,3,4] 
# for row in arr_2d:
#     # [1,2,3,4] 내부의 요소 조회
#     for elem in row:
#         print(elem, end=" ")
#     print()

# list ver
# n = list(map(int, input().split()))
# arr_2d = [
#     [0 for _ in range(n[1])]
#     for _ in range(n[0])
# ]

# tuple ver
n, m = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()