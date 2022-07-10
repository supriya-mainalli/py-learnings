# https://www.geeksforgeeks.org/python-program-to-square-each-odd-number-in-a-list-using-list-comprehension/

mylist = [1, 2, 3, 4, 5, 6, 7]

result = [x * x for x in mylist if x % 2 != 0]

print(result)
