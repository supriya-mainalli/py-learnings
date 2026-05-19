def countFrequencies(nums):
    my_dict = {}
    my_list = []

    for item in nums:
        my_dict[item] = my_dict.get(item, 0) + 1
    
    # print(my_dict)
    
    for k,v in my_dict.items():
        my_list.append([[k,v]])

    return my_list

print(countFrequencies([1, 2, 2, 1, 3]))