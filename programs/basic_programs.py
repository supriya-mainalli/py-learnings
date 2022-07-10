# reverse a string
mystr = "supriya"
print(mystr[::-1])  # same applies to reversing list

# reverse a string without any built in method or slicing
rev_str = " "
for item in "supriya":
    rev_str = item + rev_str

print("The reversed string is {}".format(rev_str))

# display only odd index values
mylist = [10, 13, 11, 45, 89]
print("The odd index values are {}".format(mylist[::2]))

# print odd or even number in list using list comprehension
mylist2 = [10, 13, 11, 45, 89, 99, 88]
mylist2 = [item for item in mylist2 if item % 2 == 0]
print("The even numbers are {}".format(mylist2))

# multiply-numbers-list
result = 1
list1 = [1, 2, 3]
for item in list1:
    result *= item
print("The multiply number list is {}".format(result))
