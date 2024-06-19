a, b = tuple(map(int, input().split()))
n = input()
result = []
num = 0
# a진수를 10진수로 변환
for temp in n:
    # 문자를 숫자로 바꿔서 진수 변환해줌
    num = num * a + ord(temp)-ord('0')

# 10진수를 b진수로 변환
while True:
    if num < b:
        result.append(num)
        break
    result.append(num%b)
    num //= b

for res in result[::-1]:
    print(res, end="")