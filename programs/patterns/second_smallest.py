import sys


def second_smallest(nums):
    fsmallest = nums[0]
    ssmallest = sys.maxsize
    for item in range(1, len(nums)):
        if nums[item] < fsmallest:
            ssmallest = fsmallest
            fsmallest = nums[item]
        elif nums[item] < ssmallest and nums[item] > fsmallest:
            ssmallest = nums[item]
        else:
            ssmallest = -1
        return ssmallest


print(second_smallest([1, 2, 4, 3, 2, 6, 7]))
