# https://leetcode.com/problems/palindrome-number/

def is_palindrome(x):
    if str(x) != str(x)[::-1]:
        return False
    return True


print(is_palindrome(-121))
