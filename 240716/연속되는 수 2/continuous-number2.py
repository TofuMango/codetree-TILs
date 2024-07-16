# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

# 연속하여 동일한 숫자가 나오는 횟수를 구함
# 그 중 최댓값을 갱신
ans, cnt = 0, 0
for i in range(n):
	# Case 1 연속한 두 원소가 일치하면 +1
	if i >= 1 and arr[i] == arr[i - 1]:
		cnt += 1
	# Case 2 일치하지 않으면 cnt 1
	else:
		cnt = 1
	# ans와 현재 cnt 값 비교해서 큰수를 ans에 저장
	ans = max(ans, cnt)

print(ans)