a, b = tuple(map(int, input().split()))

# 조건1
def findNum369(n):
    n1 = n % 10
    n2 = n // 10
    return n1 == 3 or n1 == 6 or n1 == 9 or n2 == 3 or n2 == 6 or n2 == 9
# 조건2
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