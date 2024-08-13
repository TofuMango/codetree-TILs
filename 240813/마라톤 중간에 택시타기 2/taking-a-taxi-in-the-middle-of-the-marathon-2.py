import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
	list(map(int, input().split()))
	for _ in range(n)
]

# 각 i번째 체크포인트를 건너 뛰었을 때의 거리를 구해줌
ans = INT_MAX
for i in range(1, n - 1):
	# 거리를 구함
	dist = 0
    prev_idx = 0
	for j in range(1, n):
		if j == i:
			continue
		dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1] - arr[j][1])
	    # 이전 인덱스 j를 저장   
        prev_idx = j
	
	ans = min(ans, dist)

# 출력
print(ans)
# INT_MAX = sys.maxsize
# min_total = INT_MAX
# n = int(input())
# arr = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]
# # 건너뛸 체크포인트 선택
# # 처음과 끝은 건너뛰지 않으니까 범위를 1, n-1로 잡아줌
# for skip in range(1, n-1):
#     # 합산거리
#     total = 0
#     # 순서대로 방문하며 거리계산
#     for i in range(n-1):
#         if i == skip:
#             continue
#         if i+1 == skip:
#             total += abs(arr[i][0]-arr[i+2][0])+abs(arr[i][1]-arr[i+2][1])
#         else:
#             total += abs(arr[i][0]-arr[i+1][0])+abs(arr[i][1]-arr[i+1][1])
#     min_total = min(min_total, total)
# print(min_total)