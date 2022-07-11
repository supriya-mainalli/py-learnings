# https://www.geeksforgeeks.org/remove-common-elements-from-two-list-in-python/

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, ]

list1, list2 = [x for x in list1 if x not in list2], [y for y in list2 if y not in list1]

print(list1+list2)
