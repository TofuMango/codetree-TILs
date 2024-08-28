n = int(input())

# 입력된 질문과 카운트 정보를 저장
queries = []
for _ in range(n):
    num, count1, count2 = tuple(map(int, input().split()))
    queries.append((str(num), count1, count2))

# 가능한 모든 세 자리 수 조합을 생성
possible_numbers = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:  # 서로 다른 숫자 조건
                possible_numbers.append(str(i) + str(j) + str(k))

def count_matches(secret, guess):
    exact_count = 0
    non_exact_count = 0
    
    # 정확한 자리 비교
    for i in range(3):
        if secret[i] == guess[i]:
            exact_count += 1
            
    # 다른 자리에서의 숫자 비교
    for digit in guess:
        if digit in secret:
            # 다른 자리에서 일치하는 경우
            if secret[guess.index(digit)] != digit:
                non_exact_count += 1
                
    return exact_count, non_exact_count

# 가능한 숫자 중에서 유효한 숫자 카운트
valid_count = 0

for number in possible_numbers:
    is_valid = True
    for query in queries:
        guess = query[0]
        count1 = query[1]
        count2 = query[2]
        
        exact_count, non_exact_count = count_matches(number, guess)
        
        if exact_count != count1 or non_exact_count != count2:
            is_valid = False
            break
            
    if is_valid:
        valid_count += 1

print(valid_count)