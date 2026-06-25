nums = [1,2,3,4,5,6,7]

# brute force
def rotate_arr(nums, k):
    n = len(nums)
    k = k%n
    temp1 = nums[:-k]
    temp2 = nums[-k:]
    return temp2 + temp1

# print(rotate_arr(nums, 3))

# in place modify list
def rotate_arrys(nums):
    n = len(nums)
    k = k%n
    temp = nums[:k]

    for i in range(k):
        nums[i] = nums[i-k]
    # print(nums)
    print(temp)

print(rotate_arr(nums, 3))