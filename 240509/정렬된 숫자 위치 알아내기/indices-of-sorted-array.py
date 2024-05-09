# 수열의 길이 n
n = int(input())
# 수열 입력받기
numList = list(map(int, input().split()))
sortNum = sorted(numList)

# 인덱스 매핑하기
index_map = {}
for idx, value in enumerate(sortNum):
    if value not in index_map:
        index_map[value] = [idx + 1]
    else:
        index_map[value].append(idx + 1)

# index와 기존 수열 비교하며 출력
for value in numList:
    print(index_map[value][0], end=" ")
    index_map[value].pop(0)  # 이미 사용한 인덱스는 제거

# 수열의 길이 n
# n = int(input())
# # 수열 입력받기
# numList = list(map(int, input().split()))
# sortNum = sorted(numList)
# index = []
# # 인덱스 부여하기
# for i in enumerate(sortNum, start=1):
#     index.append(i)
# # index와 기존 수열 비교
# for i in range(n):
#     for j in range(n):
#         if(numList[i]== index[j][1]):
#             print(index[j][0], end=" ")
#         else:
#             continue