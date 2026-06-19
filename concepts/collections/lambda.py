names = ["viod", "vina", "ria", "priya", "manjumainalli"]

a = sorted(names, key=len)
print(a)


# sort names based on the second char

custom_sort = lambda x: x[1:]
second_char_sort = sorted(names, key=custom_sort)
print(second_char_sort)


# sort array with frequency
arr = [1, 3, 3, 3,5,5]
my_dict = {}

for item in arr:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)

sorted_freq = sorted(arr, key= lambda x: my_dict[x], reverse=True)
print(sorted_freq)

