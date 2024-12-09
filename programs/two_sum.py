nums=[4,5,6]
target=10


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(two_sum(nums, target))
