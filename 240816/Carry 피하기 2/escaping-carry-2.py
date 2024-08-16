import sys
INT_MAX = -sys.maxsize
ans = INT_MAX
# 입력받을 숫자의 개수
n = int(input())

# 숫자를 리스트로 저장 (자릿수 순서로)
arr = [
    list(map(int, str(input().strip()[::-1])))  # 입력받은 숫자를 뒤집어서 자릿수 순서로 저장
    for _ in range(n)
]

# 각 자리별 합계를 hap에 저장하는 함수
def carry(x, y, z):
    # 각 숫자의 자릿수를 가져오고, 가장 긴 자릿수의 길이 구하기
    max_length = max(len(arr[x]), len(arr[y]), len(arr[z]))
    # 결과를 저장할 리스트 초기화
    hap = []
    
    # 각 자리수 합계를 계산
    for i in range(max_length):
        # 각 자릿수의 값을 가져오고, 없으면 0으로 채움
        digit_x = arr[x][i] if i < len(arr[x]) else 0
        digit_y = arr[y][i] if i < len(arr[y]) else 0
        digit_z = arr[z][i] if i < len(arr[z]) else 0
        
        # 각 자리수의 합을 계산
        total = digit_x + digit_y + digit_z
        
        # 만약 10의 자리를 넘어가면
        if total >= 10:
            return -1  # -1 리턴하여 종료
        
        # 10의 자리를 안 넘으면 total을 합 리스트에 추가
        hap.append(str(total))  # 합계를 hap 리스트에 추가
    
    # hap 리스트에 각 자릿수의 합이 저장되었다면 함수의 리턴값으로 hap을 리턴
    return int(''.join(hap[::-1]))

# 조합을 통해 carry 함수를 사용하여 합계 계산
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):  # j + 1로 변경하여 인접하지 않도록 함
            hap = carry(i, j, k)
            ans = max(ans, hap)
print(ans)