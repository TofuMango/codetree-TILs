offerset = 1000
max_space = 2000

# 입력
n = int(input())

# 현재 위치
cur = 0

# 이동 정보 입력받기
for _ in range(n):
    x, y = tuple(input().split())
    x = int(x)
    # 왼쪽으로 이동한 경우
    if y == 'L':
        # 왼쪽값은 빼주고
        section_left = cur - x
        # 우측은 현재값으로 업데이트(이동전 위치 저장)
        section_right = cur
        # 현재값에 이동한만큼 빼줌(이동후 위치 저장)
        cur -= x

    if y == 'R':
        section_left = cur
        section_right = cur + x
        cur += x
    # R 5면 0에서 시작한다고 가정할때..left 0 right 5해서 [0, 5]가 되겠지?
    segments.append([section_left, section_right])

res = [0] * (max_space + 1)

for x1, x2 in segments:
    x = int(x)
    # OFFSET을 더해줌, 음수위치를 양수 위치로 전환
	x1, x2 = x1 + OFFSET, x2 + OFFSET
    for i in range(x1, x2):
        res[i]+=1
# 2번 이상 지나간 영역 칠하기
cnt = 0
for r in res:
    if r >= 2:
        cnt += 1
print(cnt)