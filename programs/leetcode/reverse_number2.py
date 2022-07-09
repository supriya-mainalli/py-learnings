def reverse(number):
    rev = 0
    while number > 0:
        rev = rev * 10 + number % 10
        number = number // 10

    return rev


print(reverse(234))
