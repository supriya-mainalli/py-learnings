# https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

""" Program to check if string is palindrome or not"""

def is_palindrome(my_str):
    if my_str == my_str[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("madam"))


