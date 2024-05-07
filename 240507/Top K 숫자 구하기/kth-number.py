n, k = tuple(map(int, input().split()))
numList = list(map(int, input().split()))

# 정렬하기
numList.sort()
# k번째 숫자 출력
print(numList[k-1])