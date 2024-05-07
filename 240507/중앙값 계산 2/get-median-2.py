n = int(input())
numList = list(map(int, input().split()))

for i in range(n+1):
    if i % 2 != 0:
        tem = sorted(numList[0:n])
        print(numList[i//2], end=' ')