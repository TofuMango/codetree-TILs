# 변수 선언 및 입력
n = int(input())
arr = [
	tuple(map(int, input().split()))
	for _ in range(n)
]

# 모든 숫자 다 만들어봄
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # 같은 수가 있는지 확인하기
            # 서로 다른 수로 구성되어야하기때문
            if i == j or j == k or k == i:
                continue
            # 만약 해당 숫자가 정답이라면 모든 입력에 대해 만족하는지 확인
            succeeded = True
            for a, num_cnt1, num_cnt2 in arr:
                # a의 각 자리별 숫자 뜯기
                # 백의자리
                x = a // 100
                # 십의자리
                y = a // 10 % 10
                # 일의자리
                z = a % 10
                
                # 1번카운트, 2번카운트 초기화
                cnt1 = 0
                cnt2 = 0
                # A가 생각한 숫자와 같고 동일한 위치에 자리할때
                if x == i:
                    cnt1 += 1
                if y == j:
                    cnt1 += 1
                if z == k:
                    cnt1 += 1
                # A가 생각한 숫자와 위치는 다르지만 세자리에 해당하는 숫자가 있을때
                # 백의자리는 십의자리/일의자리 숫자 중 하나와 동일한경우
                if x == j or x == k:
                    cnt2 += 1
                if y == i or y == k:
                    cnt2 += 1
                if z == i or z == j:
                    cnt2 += 1
                
                # 만약 직접 카운트한것과 주어진 카운트 수가 다르다면
                # 해당숫자는 정답이 될수없음
                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    succeeded = False
                    break
            if succeeded:
                cnt += 1
print(cnt)