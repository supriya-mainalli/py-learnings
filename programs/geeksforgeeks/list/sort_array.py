test_list = [12, 67, 98, 34]

n = len(test_list)
index = 0
while index < n - 1:
    if test_list[index] > test_list[index + 1]:
        test_list[index], test_list[index + 1] = test_list[index + 1], test_list[index]
        index = -1
    index += 1

print(test_list)
