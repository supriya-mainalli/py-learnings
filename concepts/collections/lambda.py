names = ["viod", "vina", "ria", "priya", "manjumainalli"]

a = sorted(names, key=len)
print(a)


# sort names based on the second char

custom_sort = lambda x: x[1:]
second_char_sort = sorted(names, key=custom_sort)
print(second_char_sort)
