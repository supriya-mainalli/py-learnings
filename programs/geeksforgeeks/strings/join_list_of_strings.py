# https://www.geeksforgeeks.org/python-program-split-join-string/

list1 = ['Geeks', 'for', 'Geeks']

print("-".join(list1))

# Split the string into list of strings

input = "Geeks for Geeks"

print(input.split(" "))
new_str = input.split(" ")
new_str.sort()
print(new_str)
