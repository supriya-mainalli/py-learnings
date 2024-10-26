# https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

# Program to check if string is palindrome or symmentrical


def check_palindrome_or_symmetrical(my_string):
    if my_string == my_string[::-1]:
        print("The string is palindrome")

check_palindrome_or_symmetrical("madam")