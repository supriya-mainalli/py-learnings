def containsDuplicate(nums):
    my_dict = {}
    for item in nums:
        print(nums, item)
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    print(f"My dict is {my_dict}")
    for key in my_dict.keys():
        if my_dict[key] > 1:
            return True
    return False


print(containsDuplicate([2, 14, 18, 22, 22]))
