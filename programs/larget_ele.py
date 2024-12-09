my_list = [1,5,3,6,7,8,10]

larget_num = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > larget_num:
        larget_num = my_list[i]
print(larget_num)