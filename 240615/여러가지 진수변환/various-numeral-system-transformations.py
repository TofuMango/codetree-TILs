n, b = tuple(map(int, input().split()))
arr = []
while True:
    if n == 0:
        break
    if n<2:
        arr.append(n)
        break
    arr.append(n%b)
    n //= b
for res in arr[::-1]:
    print(res, end='')