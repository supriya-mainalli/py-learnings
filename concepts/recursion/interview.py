# EPAM find closest number

def closest(nums):
    min = 2**31-1
    pair = (None, None)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            diff = abs(nums[j] - nums[i])
            # print(nums[i], nums[j])
            if diff<min:
                min = diff
                pair = (nums[i], nums[j])
    return pair
print(closest([10, 2, 7, 4, 15, 72, 81]))
