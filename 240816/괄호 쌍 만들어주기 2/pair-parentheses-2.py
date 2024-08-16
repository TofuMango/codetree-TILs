a = input().strip()  # 입력받은 문자열에서 공백 제거
open_count = 0
pair_count = 0

for char in a:
    if char == '(':
        open_count += 1  # 여는 괄호를 세기
    elif char == ')':
        if open_count > 1:  # 여는 괄호가 있을 때만 쌍을 만들 수 있음
            pair_count += 1  # 쌍을 하나 찾음
            open_count -= 1  # 여는 괄호 하나 제거

print(pair_count)