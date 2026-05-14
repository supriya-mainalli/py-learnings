def is_anagram(s1, s2):
    print(sorted(s1))
    return sorted(s1)==sorted(s2)

# print(is_anagram('test', 'ttes'))

def is_anagram2(str1, str2):
    clean = lambda s: s.replace(" ", "").lower()

    if len(clean(str1))!=len(clean(str2)):
        return False
    
    dict1,dict2 ={}, {}
    for item in str1:
        dict1[item] = dict1.get(item, 0)+1
    for item in str2:
        dict2[item] = dict2.get(item, 0)+1
    print('************')
    print(dict1, dict2)
    return dict1==dict2

# print(is_anagram2('test', 'ttes'))

def first_unique(mystr):
    if not mystr:
        return -1
    
    mydict = {}
    for item in mystr:
        mydict[item] = mydict.get(item, 0) + 1

    for item in mydict:
        if mydict[item] == 1:
            return item
    return -1

# print(first_unique('ssuuppriia'))

# mylist = [1,2,3,2,2,3,4,8]
mylist = 'ssuuppriya'
from collections import Counter

result = Counter(mylist)
# print(result)

for item in mylist:
    if result[item] ==1:
        print(item)
        break

my_number = 12345
n = abs(my_number)
result = 0
while n>0:
    digit = n%10
    result = result*10+digit
    n = n//10
# print(result)



def is_even(mynum):
    return mynum%2==0

# print(is_even(5))


def is_adult(age):
   return "minor" if age<18 else "major"

# print(is_adult(12))

for item in range(1,10):
    print(item)


def fibnoci(nums):
    a,b = 0,1
    for item in range(2, nums+1):
        a,b = b, a+b
    print(b)

print(fibnoci(6))