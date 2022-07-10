# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

def swap_number(mylist):
    if len(mylist) > 1:
        mylist[0], mylist[-1] = mylist[-1], mylist[0]
        return mylist
    else:
        return "Swapping not possible"


print(swap_number([12, 35, 9, 56, 24]))
