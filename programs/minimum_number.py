# Write a program to find the minimum number in list

mylist = [23, 12, 11, 7, 6, 89]

minimum_number = mylist[0]

for item in range(1, len(mylist)):
    if minimum_number > mylist[item]:
        minimum_number = mylist[item]

print("The min number in list is {} ".format(minimum_number))
