N = list(map(int, input()))
num = 0
res = []
# 10진수로 변환하기
for i in range(len(N)):
    num = num * 2 + N[i]
# 10진수로 변환후 17배
num = num * 17
# 2진수 변환
while True:
    if num<2:
        res.append(num)
        break
    res.append(num%2)
    num //= 2
for r in res[::-1]:
    print(r, end='')