my_str1 ='supriya'

def reverse_str(my_str):
    new_str = ''
    for item in my_str:
        new_str = item + new_str
    return new_str


print(reverse_str(my_str1))