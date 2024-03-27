# 풀이1
# 2차원 배열 선언
# arr_2d = [
#     list(map(int, input().split()))
#     for _ in range(2)
# ]

# # 합계 변수 초기화
# sum1 = 0

# #가로 평균 구하기
# list1 = []
# for i in range(2):
#     sum1 = 0
#     for j in range(4):
#         sum1 += arr_2d[i][j]
#     average = sum1 / 4 #평균 계산
#     list1.append(average)
# print(*list1)    
        

# list2 = []
# # 세로 평균 구하기
# for i in range(4):  # 첫 번째 행의 길이(=열의 개수)만큼 반복
#     sum1 = 0
#     for j in range(2):  # 두 행을 순회
#         sum1 += arr_2d[j][i]
#     average = sum1 / 2  # 평균 계산
#     list2.append(average)
# print(*list2)

# sum1 = 0
# #전체평균
# for i in range(2):
#     for j in range(4):
#         sum1 += arr_2d[i][j]
# average = sum1 / 8
# print(round(average,1))

#풀이2
# 2차원 배열 선언
arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

#가로 평균 구하기
list1 = []
for i in range(2):
    sum1 = 0
    for j in range(4):
        sum1 += arr_2d[i][j]
    # print(sum1/4, end=" ")
    print(f"{sum1 / 4:.1f}", end=" ")
print()
#     average = sum1 / 4 #평균 계산
#     list1.append(average)
# print(*list1)    
        

list2 = []
# 세로 평균 구하기
for i in range(4):  # 첫 번째 행의 길이(=열의 개수)만큼 반복
    sum1 = 0
    for j in range(2):  # 두 행을 순회
        sum1 += arr_2d[j][i]
    # print(sum1/2, end=" ")
    print(f"{sum1 / 2:.1f}", end=" ")
print()
#     average = sum1 / 2  # 평균 계산
#     list2.append(average)
# print(*list2)

sum1 = 0
#전체평균
for i in range(2):
    for j in range(4):
        sum1 += arr_2d[i][j]
print(f"{sum1/8:.1f}")
# average = sum1 / 8
# print(average)