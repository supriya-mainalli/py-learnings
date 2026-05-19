def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return nums

# print(bubble_sort([3,5,8,1]))

# def sortings(nums):
#     n = len(nums)
#     i = 0
#     while i<=n:
#         if nums[i]


