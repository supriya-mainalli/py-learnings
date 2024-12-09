# reversing list using stack method

my_list = [1,3,89,67,96,56,93]
i = 0
list_size = len(my_list)
new_list = []
while my_list:
    print(my_list)
    # print(i, len(my_list))
    new_list.append(my_list.pop())

print(new_list)