input = """Hi
Good afternoon
My name is Supriya
Bye"""

output = """
Hi
afternoon Good
Supriya is name My
Bye"""

# new_str = " "
my_list = input.split("\n")
for item in my_list:
    new_list = item.split(" ")
    a = list(reversed(new_list))
    new_str = " ".join(a)
    print(new_str)



# n = 0
# result = []
# for item in input:
#     result.append([x[n] for x in input])
#     print(result)
#     n += 1

# print(result)

input = [[1, 2, 5], [5, 2, 1], [0, 9, 6]]
result = []

row = len(input)
col = len(input[0])
for i in range(row):
    for j in range(col):
        if i == 0:
            result.append([input[i][j]])
        else:
            result[j].append(input[i][j])
# print(result)

"""
2. input: dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']
output : {3: ['abc', 'cab'], 4: ['abcd', 'dcba'], 5: ['abcde']}
"""

dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']

my_dict = {}
new_list = sorted(dct_list, key=len)

for item in new_list:
    if len(item) not in my_dict:
        my_dict[len(item)] = list([item])
    else:
        my_dict[len(item)].append(item)
print(my_dict)

"""
input = 
doc1 = {"python": 3, "java": 2}
doc2 = {"python": 5, "c++": 4}

output = {"python": 8, "java": 2, "c++": 4}
"""

doc1 = {"python": 3, "java": 2}
doc2 = {"python": 5, "c++": 4}

result = dict(doc1)

for k,v in doc2.items():
	if k in result:
		result[k]=result.get(k) + v
	else:
		result[k] = v
print(result)


"""
3. my_list = ["eat", "tea", "tan", "ate", "nat", "bat"]   
output = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
"""
def group_anagram(my_list):
    my_dict = {}
    for item in my_list:
        k = sorted(item)
        key = "".join(k)
        if key in my_dict:
            my_dict[key].append(item)
        else:
            my_dict[key] = [item]
    return list(my_dict.values())

my_list = ["eat", "tea", "tan", "ate", "nat", "bat"]      
print('the anagram is ',group_anagram(my_list))

"""
nums = [1, 5, 7, -1, 5], target = 6
"""

def two_sums(nums, target):
	seen = set()
	result = []
	for index in range(len(nums)):
		diff = target - nums[index]
		if diff not in seen:
			seen.add(nums[index])
		else:
			result.append((diff, nums[index]))
			seen.remove(diff)
	return result

nums = [1, 5, 7, -1, 5]

print(two_sums(nums, 6))

			