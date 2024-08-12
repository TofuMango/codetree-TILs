# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    input().split()
    for _ in range(n)
]

# 이동 시에 행과 열이 전부 증가하도록
cnt = 0
# 0,0 시작이니까 최소 1,1로 이동
for i in range(1, n):
    for j in range(1, m):
        # k는 행, l은 열/ 즉 중간 점 설정하는 반복문임
        # (i,j)다음 위치부터 시작해서 마지막 행열 전까지 탐색
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줌
                # 현재위치인 0,0 와 첫번째 중간위치 (i,j) 색이 다르고
                # 첫번째 중간위치(i,j)와 두번째 중간위치(k,l) 색이 다르며
                # 두번째 중간위치와 마지막 위치의 색이 다를때만 cnt += 1
                # n-1해준건 인덱스 보정임
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[n - 1][m - 1]:
                    cnt += 1
                        
print(cnt)