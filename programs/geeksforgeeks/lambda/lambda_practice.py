# 1. Write a python program to generate a function to double a specified number.
# number = 27.2
# output = 54.4

double_number = lambda x: x * 2

print(double_number(27.2))

# 2. Write a python program to generate a function to get the power of a specified number.

power_of_3 = lambda x: 3 * x

print(list(map(power_of_3, [5, 6, 7])))

# 3. n_programmer = [('Python', 198), ('C', 112), ('R', 67)]
# output - [('R', 67), ('C', 112), ('Python', 198)]
n = [('Python', 198), ('C', 112), ('R', 67)]
n.sort(key=lambda x: x[1])
print(n)

# 4. Write a python program to generate a lambda function to check whether a given string is a number or not.
# Example of Expected Answer:
# Is the given 3687 a number: True
# Is the given Python a number: False

is_num = lambda x: type(x) == int
print(is_num(123))

# 5. Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
lst = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst = sorted(lst, key=lambda x: x[1:])
print(lst)

# 6. Using sorted() function and lambda sort the tuples in the list based on the last character of the second items.
lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
       (1805832, "West Virginia"), (39865590, "California")]
# Type your answer here.

lst = sorted(lst, key=lambda x: x[1][-1])
print(lst)
