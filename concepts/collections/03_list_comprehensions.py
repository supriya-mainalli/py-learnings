# [expression for item in iterable if condition]

# 01 Simple List Comprehension
# Generate a list of squares of numbers from 0 to 9.

squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 02 List Comprehension with condition
# Generate a list of squares of numbers from 0 to 9 if the number is even

squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# 03 List Comprehension with Multiple Conditions
# Generate a list of numbers from 0 to 9 that are both even and divisible by 3.

result = [x ** 2 for x in range(10) if x % 2 == 0 and x % 3 == 0]
print(result)  # [0, 36]


names = ['vinod', 'manju', 'maruthi', 'ria']
names = [d.upper() for d in names]

""" Return value if the item is int or float and the value is even number"""

data = [45, 9874, 'jfgh', 'ufdf', 56,0.98]
data = [x for x in data if type(x) in (int,float) and x%2==0]
print(data, names)