MAX_NUM = 10000

# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)
    # 만약 c가 G이면 1이고 아님 2
    arr[x] = 1 if c == 'G' else 2
# 모든 구간의 시작점 잡기
max_sum = 0
for i in range(MAX_NUM - k + 1):
    sum_interval = 0
    for j in range(i, i + k + 1):
        sum_interval += arr[j]

    # 최댓값을 구합니다.
    max_sum = max(max_sum, sum_interval)
                        
print(max_sum)
# max_place = 10000
# # 입력
# n, k = map(int, input().split())
# people = [
#     tuple(input().split())
#     for _ in range(n)
# ]
# arr = [0] * (max_place + 1)

# # arr 배열에 정보 저장
# last = 0
# for elem1, elem2 in people:
#     elem1 = int(elem1)
#     if elem2 == 'G':
#         elem2 = 1
#     elif elem2 == 'H':
#         elem2 = 2
#     else:
#         elem2 = 0
#     arr[elem1] = elem2
#     last = max(elem1, last)
# if k >= last:
#     last = k
# # 사진 크기별 최대 점수 구하는 로직
# ans = 0
# for i in range(1, last - k + 2):
#     tmp_ans = 0
#     for j in range(i, i+k+1):  # i부터 i+k-1까지
#         tmp_ans += arr[j]  # arr[j]에서 점수를 더함
#     ans = max(tmp_ans, ans)

# print(ans)