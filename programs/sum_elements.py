def total(nums):
    sum = 0
    for item in nums:
        sum+=item
    return sum

# print(total([1,2,3,4,5,5,66,7,7]))

def find_max(nums):
    max_num = nums[0]
    for item in nums:
        if item>max_num:
            max_num = item
    return max_num

def remove_dups(nums):
    return list(set(nums))

def remove_dups1(nums):
    new_list = []
    if not nums:
        return []
    for item in nums:
        if item not in new_list:
            new_list.append(item)
    return new_list

# print(remove_dups1([1,1,2,2,3,4,5,5]))

def occurances(nums):
    mydict = {}
    for item in nums:
        mydict[item] = mydict.get(item, 0)+1
    return mydict
    
def flatten(l1):
    new_list = []
    for item in l1:
        new_list.extend(item)
    return new_list
# print(flatten([[1,2],[3,4],[4,4],[1]]))

def two_sum(nums, target):
    my_dict = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in my_dict:
            return [i, my_dict[diff]]
        my_dict[nums[i]] = i


# print(two_sum([2, 7, 11, 15], 9))

def rotate(nums, k):
    count = k%len(nums)
    if count == 0:
        return nums
    l1 = nums[-(count):]
    return l1 + nums[:-(count)]

# print(rotate([1, 2, 3, 4, 5], 3))

def move_zeroes(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i]!=0:
            new_list.append(nums[i])
    print(new_list)
    count = len(nums)-len(new_list)
    return new_list + [0]*count

# print(move_zeroes([0,1,0,3,12]))

def missing(nums):
    actual_total = sum(nums)
    n = len(nums)+1
    print(n)
    expected_total = n*(n+1)//2
    return expected_total - actual_total

# print(missing([1,2]))


import json

my_dict = {'supriya':10, 'manju' : 20, 'maruthi' : 30}
res = json.dumps(my_dict)
print(res, type(res))

json.loads(res)
res1 = json.loads(res)
print(res1, type(res1))

def closest(nums):
    # min_diff = None
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-1):
            print(nums[i], nums[j])


        

print(closest([10,11,3,4]))
