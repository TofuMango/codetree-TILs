maxSpace = 1000000
result = [0] * (2*maxSpace+1)
cur = maxSpace
w, b = 0, 0
n = int(input())
for i in range(n):
    x, p = tuple(input().split())
    x = int(x)
    if p == 'R':
        while x > 0:
            result[cur] = 1
            x-=1

            if x:
                cur += 1
    else :
        while x > 0:
            result[cur] = 2
            x-=1

            if x:
                cur -= 1

for j in range(2*maxSpace+1):
    if result[j] == 1:
        b += 1
    elif result[j] == 2:
        w += 1
    else:
        continue
print(w, b)