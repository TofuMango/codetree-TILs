# 변수 선언 및 입력
n, k, t = tuple(input().split())
n, k = int(n), int(k)


# a가 b로 시작하는지를 확인합니다.
def starts_with(a, b):
    # b의 길이가 더 길 수는 없습니다.
    if len(a) < len(b):
        return False
    
    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인합니다.
    return a[:len(b)] == b


words = []
for _ in range(n):
    word = input()
    if starts_with(word, t):
        words.append(word)

# 정렬을 진행합니다.
words.sort()

print(words[k - 1])
# # 수정ver
# n, k, T = input().split()
# k = int(k)
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
#         if j[0:len(T)] == T:
#             tList.append(j)

# print(tList[k-1])

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