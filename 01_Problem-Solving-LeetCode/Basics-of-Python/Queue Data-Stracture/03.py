nums = [2,7,11,15]
# target = 9
# output = [0,1]
i = 0
while i <= len(nums):
    if nums[i] + nums[i+1] == 9:
        print([i, i+1])
    break        
        