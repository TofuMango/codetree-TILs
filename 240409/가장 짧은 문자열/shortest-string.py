str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

max = len1
min = len1

if len2 >= max:
    max = len2

if len3 >= max:
    max = len3
 
if len2 <= min:
    min = len2

if len3 <= min:
    min = len3

print(max-min)