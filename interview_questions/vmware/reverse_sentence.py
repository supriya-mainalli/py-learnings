input = """Hi
Good afternoon
My name is Supriya
Bye"""

output = """
Hi
afternoon Good
Supriya is name My
Bye"""

# new_str = " "
my_list = input.split("\n")
for item in my_list:
    new_list = item.split(" ")
    a = list(reversed(new_list))
    new_str = " ".join(a)
    print(new_str)



