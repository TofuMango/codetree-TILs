a, b = tuple(map(int, input().split()))

# 조건1
def findNum369(n):
    return n % 10 == 3 or n % 10 == 6 or n % 10 == 9
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