max_place = 100000
# 입력
n, k = map(int, input().split())
people = [
    tuple(input().split())
    for _ in range(n)
]
arr = [0] * (max_place + 1)

# arr 배열에 정보 저장
last = 0
for elem1, elem2 in people:
    elem1 = int(elem1)
    if elem2 == 'G':
        elem2 = 1
    elif elem2 == 'H':
        elem2 = 2
    else:
        elem2 = 0
    arr[elem1] = elem2
    last = max(elem1, last)
# 사진 크기별 최대 점수 구하는 로직
ans = 0
for i in range(1, last - k + 2):
    tmp_ans = 0
    for j in range(i, i+k+1):  # i부터 i+k-1까지
        tmp_ans += arr[j]  # arr[j]에서 점수를 더함
    ans = max(tmp_ans, ans)

print(ans)