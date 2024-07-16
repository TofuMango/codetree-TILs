n = int(input())
number = [0] * n
for i in range(n):
    tmp = int(input())
    number[i] = tmp

cnt = 1  # 첫 번째 요소는 무조건 그룹에 포함되므로 1로 시작
max_cnt = 0
for i in range(1, n):  # 첫 번째 요소는 이미 처리했으므로 1부터 시작
    if number[i] == number[i - 1]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1  # 새로운 그룹이 시작되므로 1로 초기화
if cnt > max_cnt:  # 마지막 그룹이 최대 그룹일 수도 있으므로 확인
    max_cnt = cnt

print(max_cnt)