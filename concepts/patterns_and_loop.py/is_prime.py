def is_prime(nums):
    for i in range(2, nums+1):
        if nums%i==0:
            print(i)

print(is_prime(36))