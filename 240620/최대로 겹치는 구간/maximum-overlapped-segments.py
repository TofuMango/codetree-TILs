n = int(input())
res = [0] * 100
for i in range(n):
    a, b = tuple(map(int, input().split()))
    if a <= 0:
        a += abs(a)
        b += abs(a)
        for j in range(a-1,b-1):
            res[j]+=1
    for j in range(a-1,b-1):
        res[j]+=1
print(max(res))