my_list = [1,2,3,4,5,5,6,8,2,3,4]

result = {}
for i in range(len(my_list)):
    result[my_list[i]] = 1 + result.get(my_list[i], 0)

print(result)