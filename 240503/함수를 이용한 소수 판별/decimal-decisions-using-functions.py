a, b = tuple(map(int, input().split()))

def findPrimeNum(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

hab = 0
for i in range(a, b+1):
    if findPrimeNum(i):
        hab += i

print(hab)