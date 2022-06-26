number = int(input("Enter the number"))


def fib(n):
    if n <= 1:
        return 1
    else:
        return n * fib(n - 1)


print(fib(number))
