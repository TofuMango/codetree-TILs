nums = list(map(int, input()))
num = 0
for i in range(len(nums)):
    num = num * 2 + nums[i]
print(num)