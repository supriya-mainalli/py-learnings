number = int(input("Enter the number"))


def factorial_number(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_number(n - 1)


print(factorial_number(number))
