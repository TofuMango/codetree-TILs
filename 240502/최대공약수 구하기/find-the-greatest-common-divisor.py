# 입력
n, m = tuple(map(int, input().split()))

# 최대공약수 구하는 함수
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(gcd)
gcd(n, m)