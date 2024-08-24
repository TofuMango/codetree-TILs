# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(,i):
# #     hap = 0
# #     cnt = 0
# #     tmp = []
# #     for j in range(i, n):
# #         hap += arr[j]
# #         cnt += 1
# #         tmp.append(arr[j])
# #     # 구간 내 원소들의 평균값
# #     hap = hap // cnt
# #     print('h', hap)
# #     print(tmp)
# #     for k in range(len(tmp)):
# #         if hap == tmp[k]:
# #             ans += 1
# #             print(ans)
# #             break
# # print(ans)
def count_average_subarrays(n, arr):
    count = 0

    # 모든 가능한 구간 탐색
    for i in range(n):
        total_sum = 0
        # j는 i부터 시작하여 n까지
        for j in range(i, n):
            total_sum += arr[j]
            length = j - i + 1
            
            # 평균 계산
            average = total_sum / length
            
            # 평균이 정수인지 확인
            if average.is_integer():
                average = int(average)  # 정수로 변환
                
                # 구간 내에 평균과 같은 값이 존재하는지 확인
                if average in arr[i:j + 1]:
                    count += 1

    return count

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = count_average_subarrays(n, arr)
print(result)