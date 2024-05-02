# n입력
N = int(input())

# 10으로 나눈 값 반환
def div(n):
    sum_ = 0
    for i in range(n+1):
        sum_ += i
    sum_ //= 10
    return sum_
    
# 출력
total = div(N)
print(total)

# # 변수 선언 및 입력:
# n = int(input())


# def sum_n(n):
#     sum_val = 0
#     for i in range(1, n + 1):
#         sum_val += i
    
#     return sum_val // 10


# print(sum_n(n))