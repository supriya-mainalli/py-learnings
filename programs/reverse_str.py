def reverse_str(mystr):
    str2 = ''
    for item in mystr:
        str2 =  item + str2
    return(str2)

# print(reverse_str('supriya'))

def count_vowels(mystr):
    vowels = 'aeiou'
    count = 0
    for char in mystr:
        if char in vowels:
            count +=1
    return count
# print(count_vowels('supriya'))

def reverse_number(nums):
    result = 0
    n = abs(nums)
    while n>0:
        digit = n%10
        result = result*10 + digit
        n = n//10
    return result
print(reverse_number(12345))