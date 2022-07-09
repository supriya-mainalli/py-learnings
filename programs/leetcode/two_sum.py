# https://leetcode.com/problems/two-sum/


def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]


print(two_sum([3, 2, 4, 4], 8))
