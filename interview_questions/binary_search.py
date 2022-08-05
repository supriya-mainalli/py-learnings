# https://www.geeksforgeeks.org/python-program-for-binary-search/

array1 = [2, 3, 4, 10, 40]
x = 40


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid

    return -1


print(binary_search(array1, x))
