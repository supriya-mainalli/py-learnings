# https://leetcode.com/problems/reverse-integer/

def reverse(x):
    if x < 0:
        x *= -1
        return int(str(x)[::-1]) * -1
    return str(x)[::-1]


print(reverse(-123))
