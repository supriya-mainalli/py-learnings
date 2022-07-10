# https://www.geeksforgeeks.org/python-program-to-find-cumulative-sum-of-a-list/
list1 = [10, 20, 30, 40, 50]

temp_sum = 0
list2 = []


def cumulative_sum(mylist):
    global temp_sum
    for item in mylist:
        temp_sum = temp_sum + item
        list2.append(temp_sum)

    return list2


print(cumulative_sum([10, 20, 30, 40, 50]))
