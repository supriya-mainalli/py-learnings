# Write a program to get the duplicate number count from list

mylist = [1, 1, 2, 2, 1, 2, 2, 45, 90, 12]

mydict = {}


def get_duplicate_count(mylist):
    for item in mylist:
        if item in mydict:
            mydict[item] = mydict[item] + 1
        else:
            mydict[item] = 1

    return mydict


print(get_duplicate_count(mylist))
