n = int(input())

def findNum(N):
    num1 = N // 10
    num2 = N % 10
    s = num1+num2
    # n % 2 == 0 and (n // 10 + (n % 10)) % 5 == 0 이렇게 한번에 줄이기 가능
    if N % 2 == 0 and s % 5 == 0:
        print("Yes")
    else:
        print("No")
# 함수호출
findNum(n)


# 예제
# def countNum(n):
#     return n % 3 != 0 and n%5 == 0

# cnt = 0
# for i in range(1,101):
#     if countNum(i):
#         cnt += 1
# print(cnt)