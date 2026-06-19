my_list = [3, 4, 6, 7, 9, 12, 16, 19]


def binary_search(my_list, target):
    low = 0
    high = len(my_list)-1

    while low <= high:
        mid = (low+high)//2
        if target == my_list[mid]:
            return mid
        elif target < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
print(binary_search([3, 4, 6, 7, 9, 12, 16, 19], 4))

    