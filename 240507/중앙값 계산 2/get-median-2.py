n = int(input())
numList = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        tem = sorted(numList[0:i+1])
        print(tem[i//2], end=' ')