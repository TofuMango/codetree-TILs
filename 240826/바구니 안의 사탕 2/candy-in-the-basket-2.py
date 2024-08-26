# max_len = 16
# n, k = map(int, input().split())
# arr = [0] * max_len
# for _ in range(n):
#     candy, basket = map(int, input().split())
#     arr[basket] = candy
# cnt = 0
# # 구간 확인
# # 구간 시작좌표
# for c in range(max_len):
#     lower = c - k
#     upper = c + k
#     total = 0

#     for basket, candy in 
# 입력 받기
N, K = map(int, input().split())
candies = []

# 바구니의 사탕 개수와 위치를 입력 받기
for _ in range(N):
    candy_count, position = map(int, input().split())
    candies.append((position, candy_count))

# 사탕의 수를 최대화하기 위한 변수
max_candies = 0

# 모든 가능한 중심점 c를 고려 (0부터 100까지)
for c in range(101):
    # 구간 [c-K, c+K] 설정
    lower_bound = c - K
    upper_bound = c + K
    total_candies = 0
    
    # 구간 내의 사탕 개수 계산
    for position, candy_count in candies:
        if lower_bound <= position <= upper_bound:
            total_candies += candy_count
            
    # 최대 사탕 수 업데이트
    max_candies = max(max_candies, total_candies)

# 결과 출력
print(max_candies)