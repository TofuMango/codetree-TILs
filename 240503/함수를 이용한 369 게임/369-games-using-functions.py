a, b = tuple(map(int, input().split()))

# 조건1: 숫자 안에 3, 6, 9가 포함되어 있는지 확인
def findNum369(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n //= 10  # 다음 자릿수를 검사하기 위해 10으로 나눔
    return False

# 조건2: 숫자가 3의 배수인지 또는 3, 6, 9가 포함되어 있는지 확인
def findNumber3(n):
    return n % 3 == 0 or findNum369(n)

cnt = 0
for i in range(a, b+1):
    if findNumber3(i):
        cnt += 1

print(cnt)

# cnt = 0

# def different(n):
#     return n//10 != n%10

# def findNumber(n):
#     return n % 3 != 0 and different(n)

# for i in range(10, 100):
#     if findNumber(i):
#         cnt += 1

# print(cnt)