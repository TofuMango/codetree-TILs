# 수정ver
n, k, T = input().split()
k = int(k)
# 문자열들 입력받아서 배열에 저장
arrWord = [
    list(map(str, input().split()))
    for _ in range(int(n))
]
# 배열 사전순 정렬
arrWord.sort()
# ap만 들은 list만들기
tList = []
# 문자열T로 시작하는 단어들을 배열ap에 저장
for i in arrWord:
    for j in i:
        if j[0:len(T)] == T:
            tList.append(j)

print(tList[k-1])

# 런타임 에러ver
# n, k, T = input().split()

# # 문자열들 입력받아서 배열에 저장
# arrWord = [
#     list(map(str, input().split()))
#     for _ in range(int(n))
# ]
# # 배열 사전순 정렬
# arrWord.sort()
# # ap만 들은 list만들기
# tList = []
# # 문자열T로 시작하는 단어들을 배열ap에 저장
# for i in arrWord:
#     for j in i:
#         if j[0:2] == T:
#             tList.append(j)

# print(tList[int(k)-1])