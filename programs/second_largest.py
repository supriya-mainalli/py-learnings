my_list = [1,5,3,6,7,8,10]

first_largest = my_list[0]
second_larget = -1

for i in range(1, len(my_list)):
    if my_list[i]> first_largest:
        first_largest = my_list[i]
        if second_larget > first_largest:
            second_larget, first_largest = first_largest, second_larget


print(f'The first largest number is {first_largest} and second is {second_larget}')
