# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
# source - https://www.youtube.com/watch?v=28APRkI0jsM&ab_channel=BroCode

"""
syntax:-
dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
"""

# 1.
my_dict = {"a": 2, "b": 3, "c": 10, "d": 11}

print({key: (0 if value % 2 == 0 else -1) for (key, value) in my_dict.items()})

# 2.
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
print({key: value for (key, value) in zip(keys, values)})

# 3.
my_list = [1, 2, 1, 1, 2, 33, 6, 6]

print({x: my_list.count(x) for x in my_list})
