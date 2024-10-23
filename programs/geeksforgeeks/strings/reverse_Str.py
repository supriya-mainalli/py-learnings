"""reverse string without built in method"""

def reverse_str(my_str):
    rever_str = ""
    for item in my_str:
        rever_str = item + rever_str
    return rever_str

print(reverse_str("supriya m"))
