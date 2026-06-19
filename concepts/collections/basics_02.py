# nums = [2, 7, 11, 15]

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         # print(i, j)
#         pass
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_s = {}
        my_dict_t = {}
        for i in s:
            my_dict_s[i] = my_dict_s.get(i, 0) + 1

        for i in t:
            my_dict_t[i] = my_dict_t.get(i, 0) + 1
        print(my_dict_s,my_dict_t )
        return my_dict_s == my_dict_t

# s = Solution()
# print(s.isAnagram('anagram', 'nagaram'))

# def sort_strs(my_str):
#     # a = sorted(my_str)
#     return ''.join(sorted(my_str))



# def groupAnagrams(strs):
#     my_dict = {}
#     my_list = []
#     sort_fun = lambda my_str: ''.join(sorted(my_str))

#     for item in strs:
#         print(sort_fun(item))
#         if sort_fun(item) in my_dict:
#             my_dict[sort_fun(item)] = my_dict.get(sort_fun(item)) + [item]
#         else:
#             my_dict[sort_fun(item)] = my_dict.get(sort_fun(item), [item])
#     for v in my_dict.values():
#         my_list.append(v)
#     return my_list

# print(groupAnagrams(["a"]))

def isPalindrome(s):
    new_str = ""
    for item in s:
        if item.isalpha() or item.isdigit():
            new_str += item.lower()
    

    sort_func = lambda my_str: "".join(reversed(my_str))
    print(new_str, sort_func(new_str))
    return new_str == sort_func(new_str)

print(isPalindrome('0P'))