n, m = tuple(map(int, input().split()))

def LCM(a, b):
    for i in range(max(a,b), (a*b)+1):
        if i%a == 0 and i%b == 0:
            return i

print(LCM(n, m))