# n = 4

# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# # 이건 1부터 n까지 차례로 출력하는방법.
# res = 1
# for i in range(n):
#     if i%2 == 0:
#         for j in range(n): 
#             arr_2d[i][j] = res
#             res += 1
#     else:
#         # range(a,b,c)-> a부터 b-1 범위까지 c간격으로 반복
#         for j in range(n-1,-1,-1):
#             arr_2d[i][j] = res
#             res += 1

# for row in arr_2d:
#     for col in row:
#         print(col, end=" ")
#     print()

# 숫자 입력받기
n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 일단... 배열[n][0]에 각각차례로 12345 입력받아야함.
# 입력받고나서 주어진 값만큼 증가시키는 코드 짜기

a = 1
b = 1

for i in range(n):
    for j in range(n):
        arr_2d[i][j] = i + 1 + j * n

for row in arr_2d:
    for col in row:
        print(col, end=" ")
    print()