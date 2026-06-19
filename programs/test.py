str1 = "ssagewrerassfg"

my_dict = {}

for item in str1:
    my_dict[item] = my_dict.get(item, 0) + 1


print(list(my_dict.items()))

# condition = lambda x : x[1]
# result = list(sorted(my_dict.items(), key=condition, reverse=True))
# print(result)

# print(sorted(my_dict.values()))
custom_func = lambda x : len(x)

my_list = ['supriya', 'abc', 'test', 'gdhfjagh']
print(my_list)
# print(sorted(my_list, key=custom_func))

# my_str = "hello world"
# # new_list = [x.split() for x in my_str]
# my_list = my_str.split()
# print(my_list)
# a = [x[::-1] for x in my_list]
# print(a)

my_list = [-1, -3, -4, 5]

def find_Second_largest(my_list):
    first_largest = my_list[0]
    second_largest = -1
    n = len(my_list)

    for i in range(1, n):
        if(my_list[i]>second_largest and my_list[i]<first_largest):
            second_largest = my_list[i]
        elif(my_list[i]>second_largest and my_list[i]>first_largest):
            first_largest,second_largest = my_list[i],first_largest
        else:
            pass
    return second_largest

print(f'the list is {my_list}')
print('second_largest', find_Second_largest(my_list=my_list))
