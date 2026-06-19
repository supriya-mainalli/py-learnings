import math

def list_prime(nums):
    for i in range(1, int(math.sqrt(nums))+1):
        if nums%i == 0:
            print(i)
        if (nums//i)!=i:
            print(nums//i)
# print(list_prime(36))


def divisors(n):
    my_list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            my_list.append(i)
        if (n//i)!=i:
            my_list.append(n//i)
    return my_list

print(divisors(10))