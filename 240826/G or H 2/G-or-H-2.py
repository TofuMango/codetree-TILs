MAX_NUM = 100

# 변수 선언 및 입력
n = int(input())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    # c가 G이면 1, H면 2
    arr[x] = 1 if c == 'G' else 2

# 모든 구간의 시작점 잡기
max_len = 0
# 시작점 설정
for i in range(MAX_NUM + 1):
    # i보다 j가 항상큰값이 되도록
    # 끝점설정
	for j in range(i + 1, MAX_NUM + 1):
		# i와 j 위치에 사람이 있는지 확인
		if arr[i] == 0 or arr[j] == 0:
			continue
		# 해당 구간 내 g와 h의 개수 구하기
		cnt_g = 0
		cnt_h = 0
		# 모든 구간 탐색
		for k in range(i, j + 1):
            # 현재구간의 k가 1이라면 g에 1증가
			if arr[k] == 1:
				cnt_g += 1
			if arr[k] == 2:
				cnt_h += 1
		
		# 조건을 만족할 때 구간의 길이를 구해 최댓값과 비교
		if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            # j는 끝점, i는 시작점...
			leng = j - i
			max_len = max(max_len, leng)

print(max_len)