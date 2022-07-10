# https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/

def second_max(mylist):
    temp_list = mylist
    first_max = find_max(temp_list)
    temp_list.remove(first_max)
    second_max_num = find_max(temp_list)
    return second_max_num


def find_max(mylist):
    max_number = 0
    for item in mylist:
        if item > max_number:
            max_number = item
    return max_number


print("The second max element is {}".format(second_max([10, 20, 30, 60])))
