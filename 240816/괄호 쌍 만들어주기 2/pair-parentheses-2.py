def count_pairs(s):
    open_positions = []
    pair_count = 0
    
    # 연속한 여는 괄호의 위치 찾기
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i + 1] == '(':
            open_positions.append(i)
    
    # 연속한 닫는 괄호의 개수 세기
    for start in open_positions:
        for j in range(start + 2, len(s) - 1):
            if s[j] == ')' and s[j + 1] == ')':
                pair_count += 1

    return pair_count

# 입력 받기
input_string = input().strip()
result = count_pairs(input_string)
print(result)