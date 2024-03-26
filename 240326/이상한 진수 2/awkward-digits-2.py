import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

# 각 i번째 자릿수를 바꾸었을 때의 십진수 값
ans = INT_MIN
for i in range(length):
	binary[i] = 1 - binary[i]
	num = 0
	for j in range(length):
		num = num * 2 + binary[j]
	ans = max(ans, num)
	binary[i] = 1 - binary[i]
print(ans)