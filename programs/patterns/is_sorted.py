# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


# [3, 4, 6, 1, 2, 5]
# [1, 2, 3]
def check(nums):
    orginal_list = nums
    item = 0
    while item <= len(nums) - 2:
        if nums[item + 1] >= nums[item]:
            item = item + 1
        elif (
            (nums[item] <= nums[item - 1])
            and (item == len(nums) - 1)
            and len(nums) != 2
        ):
            return False
        else:
            s_list = nums[item + 1 :]
            new_arr = nums[: item + 1]
            nums = s_list + new_arr
            if nums != orginal_list:
                item = 0
            else:
                return False
    return True


print(check([2, 7, 4, 1, 2, 6, 2]))
