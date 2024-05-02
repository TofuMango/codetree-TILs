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