def smallest_element(nums):
    selement = nums[0]
    for item in range(1, len(nums)):
        if nums[item] < selement:
            selement = nums[item]
    return selement


print(smallest_element([1, 3, 44, 2, 1, 8, -1]))
