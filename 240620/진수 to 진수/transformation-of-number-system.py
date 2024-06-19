MAX_DIGIT = 30

# 변수 선언 및 입력:
a, b = tuple(map(int, input().split()))
n = input()

digits = []

   
# 십진수로 변환
num = 0
for ch in n:
    num = num * a + (ord(ch) - ord('0'))

# b진수로 변환
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

# 진수 배열을 뒤집어 b진수를 출력
for digit in digits[::-1]:
    print(digit, end="")