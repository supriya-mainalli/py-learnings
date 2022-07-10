# https://www.geeksforgeeks.org/python-program-to-find-sum-of-array/

mylist = [15, 12, 13, 10]


def sum_of_array(mylist):
    sum = 0
    for item in mylist:
        sum += item

    return sum


print("The sum of array is {}".format(sum_of_array(mylist)))
