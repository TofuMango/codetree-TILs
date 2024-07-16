# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

# 연속하여 동일한 숫자가 나오는 횟수 구함
# 그 중 최댓값을 갱신
ans, cnt = 0, 0
for i in range(n):
	# Case 1
	# 두번째 요소부터 비교하기, 부호가 일치하면 양수가 됨(음음양 -> 음수/ 양양음 -> 음수)
	if i >= 1 and arr[i] * arr[i - 1] > 0:
		cnt += 1
	# Case 2
	# 
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)