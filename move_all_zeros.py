nums = [0, 1, 0, 3, 12]

def move_zeros(nums):
    count = 0
    res = []
    for item in nums:
        if item!=0:
            res.append(item)
        else:
            count += 1
    return res + count*[0]

print(move_zeros(nums))
        

