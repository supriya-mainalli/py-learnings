nums = [4,5,3,7,1,9]

def rotate_array_by_one(nums):
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    nums[-1] = temp
    print(nums)

print(rotate_array_by_one(nums))
    