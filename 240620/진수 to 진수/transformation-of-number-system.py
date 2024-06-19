# 입력 받기
a, b = map(int, input().split())
n = input()

# a진수를 10진수로 변환
decimal = 0
for i, digit in enumerate(n[::-1]):
    decimal += int(digit, a) * a ** i

# 10진수를 b진수로 변환
digits = "0123456789"
result = ""
while decimal > 0:
    result = digits[decimal % b] + result
    decimal //= b

# 결과 출력
print(result if result else "0")