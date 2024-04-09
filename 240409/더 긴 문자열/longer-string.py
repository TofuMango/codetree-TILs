# words = list(input().split())

# if len(words[0]) > len(words[1]):
#     print(words[0], len(words[0]))
# elif len(words[0]) == len(words[1]):
#     print("same")
# else:
#     print(words[1], len(words[1]))

# 문자열을 입력받습니다.
str1, str2 = input().split()

# 문자열의 길이를 구합니다.
len1 = len(str1)
len2 = len(str2)
	
# 더 긴 문자열과 그 문자열의 길이를 출력합니다. 같을 경우 same을 출력합니다.
if len1 > len2:
	print(str1, len1)
elif len1 < len2:
	print(str2, len2)
else:
	print("same")