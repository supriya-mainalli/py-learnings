def second_largest(nums):
    fl = nums[0]
    sl = -1
    for item in range(1, len(nums)):
        if nums[item] > fl:
            sl = fl
            fl = nums[item]
        elif nums[item] > sl and nums[item] < fl:
            sl = nums[item]
        else:
            sl = -1

    return sl


print(second_largest([3, 3, 3, 3, 3, 3]))
