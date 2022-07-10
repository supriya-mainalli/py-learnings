# https://www.geeksforgeeks.org/python-count-occurrences-element-list/

# first way
def count_number(target, mylist):
    count = 0
    for item in mylist:
        if target == item:
            count += 1
    return count


print("The {} occurred {} times.".format(8, count_number(8, [8, 6, 8, 10, 8, 20, 10, 8, 8])))

# using count method

mylist = [8, 6, 8, 10, 8, 20, 10, 8, 8]

print("Using count method ---- The {} occurred {} times.".format(8, mylist.count(8)))
