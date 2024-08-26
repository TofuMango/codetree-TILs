# n, m = int(input())
# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))

# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 수열 B의 각 원소의 개수를 세기
from collections import Counter
count_B = Counter(B)

# 아름다운 수열의 개수
beautiful_count = 0

# 수열 A에서 길이가 M인 연속 부분 수열 검사
for i in range(N - M + 1):
    sub_sequence = A[i:i + M]
    count_sub = Counter(sub_sequence)
    
    # B의 원소 개수와 일치하는지 확인
    if count_sub == count_B:
        beautiful_count += 1

# 결과 출력
print(beautiful_count)