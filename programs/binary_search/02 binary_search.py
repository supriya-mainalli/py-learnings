# Binary search through recursive way


my_list = [3, 4, 6, 7, 9, 12, 16, 19]


def bin_search2(arr, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bin_search2(arr, target, low, mid - 1)
    else:
        return bin_search2(arr, target, mid + 1, high)


print(bin_search2(my_list, 19, 0, len(my_list) - 1))
