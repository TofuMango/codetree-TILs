# 정보 입력
N, K, P, T = tuple(map(int, input().split()))
handShake = [
    tuple(map(int, input().split()))
    for _ in range(T)
]
# 시간순대로 악수상황 정렬(t가 기준)
handShake.sort(key = lambda x:x[0]) 
# 감염자 체크
infected = [0] * (N + 1)
# 감염자별 감염횟수 체크
cnt = [0] * (N + 1)
# 최초감염자 체크
infected[P] = 1
# 최초감염자의 전염 가능횟수 체크
cnt[P] = K

for t, x, y in handShake:
    # 만약 x가 감염자면서 횟수가 남아있을때
    if infected[x] == 1 and cnt[x] > 0:
        # y가 감염자가 아니었다면:
        if infected[y] == 0:
            # y를 감염시키고
            infected[y] = 1
            # y의 감염 가능횟수 체크하고
            cnt[y] = K
            # x의 감염 가능횟수는 차감하기
            cnt[x] -= 1
        # y가 감염자였다면
        else:
            # x,y의 감염가능횟수 둘다 차감
            cnt[x] -= 1
            cnt[y] -= 1
    # 만약 y가 감염자면서 횟수가 남아있을때
    elif infected[y] == 1 and cnt[y] > 0:
        # x가 감염자가 아니었다면
        if infected[x] == 0:
            # x를 감염시키고
            infected[x] = 1
            # x의 감염 가능횟수 체크하고
            cnt[x] = K
            # y의 감염 가능횟수는 차감하기
            cnt[y] -= 1
        # x가 감염자였다면
        else:
            # x,y의 감염가능횟수 둘다 차감
            cnt[x] -= 1
            cnt[y] -= 1

# 결과 출력
print("".join(map(str, infected[1:])))