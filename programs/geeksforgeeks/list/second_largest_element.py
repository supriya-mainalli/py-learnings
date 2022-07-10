# https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/

# first way to sort and take second element
mylist = [10, 20, 4, 45, 99, 100]


def second_max(mylist):
    mylist.sort()
    return mylist[-2]


print(second_max(mylist))
