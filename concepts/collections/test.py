# two sum

def two_sum(nums, target):
    my_dict = {}

    for index in range(len(nums)):
        diff = target - nums[index]

        if diff in my_dict:
            return [index, my_dict[diff]]
        else:
            my_dict[nums[index]] = index
    print(my_dict)
# print(two_sum([1,0,8,10,7], 18))

def second_larget(nums):
    first_larget = nums[0]
    second_larget = -1
    for item in range(1, len(nums)):
        if nums[item] > first_larget:
            first_larget, second_larget = nums[item], first_larget
        elif (nums[item] < first_larget) and (nums[item] > second_larget):
            second_larget = nums[item]
        print('iterations',first_larget, second_larget)
    return [first_larget, second_larget]

# print(second_larget([200,7,6,10,8,9,21, 54, 34, 56, 100]))

def second_smallest(nums):
    first_smallest = nums[0]
    s_smallest = 2**31-1

    for index in range(1, len(nums)):
        if nums[index]<first_smallest:
            first_smallest = nums[index]
        elif nums[index] < s_smallest and nums[index] > first_smallest:
            s_smallest = nums[index]
        print(first_smallest, s_smallest)
            

# print(second_smallest([45,24,2, 10, 13, 41,12]))                                  

def binary_search(nums, target):
    low = 0
    n = len(nums)
    high = n - 1

    while(low<=high):
        mid = (low+high)//2
        if mid == target:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid - 1
    return -1 # element not found
# print(binary_search([10,14,17,30,40,70], 117))

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-1-i):
            if nums[j+1]> nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums
# print(bubble_sort([5, 3, 1, 4, 2]))


def is_prime(num):
    if num<=1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
        return True
# print(is_prime(6))

def fib(num):
    if num<=1:
        return 1
    return num*fib(num-1)
# print(fib(3))

str1 = '''hi this is supriya python programming'''
# supriya is this hi
new_list = str1.split(' ')
new_str = ""
n = len(new_list)-1
while n >= 0:
    new_str = new_str + new_list[n]+ " "
    n -= 1
# print(new_str.strip())

max_element = 0
new_str1 = ""
for item in new_list:
    if len(item) > max_element:
        max_element, new_str1 = len(item), item
# print(item)


def balanced_pare(new_str):
    open_brackets = '({['
    closed_brackets = ']})'
    matching_braces = {
        '(': ')',
        '{' : '}',
        '[': ']'
    }

    stack = []

    for item in new_str:
        if item in open_brackets:
            stack.append(item)
        elif(item in closed_brackets and matching_braces[stack[-1]]==item):
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
print(balanced_pare('{()}'))