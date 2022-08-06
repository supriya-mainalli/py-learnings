"""
1. input = [[1,2,5],[5,2,1],[0,9,6]]
output = [[1,5,0],[2,2,9],[5,1,6]]
"""




"""
2. input: dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']
output : {3: ['abc', 'cab'], 4: ['abcd', 'dcba'], 5: ['abcde']}
"""
my_dict = {}
dct_list = ['abc', 'cab', 'abcd', 'dcba', 'abcde']
for item in dct_list:
    if len(item) not in my_dict:
        my_dict[len(item)] = list([item])
    else:
        my_dict[len(item)].append(item)

print(my_dict)

"""
3.my_str = "My name is supriya M"
output = "Ma yirp us siemany M"
"""
my_str = "My name is supriya M"


def reverse_str(my_str):
    my_list = my_str.split(" ")
    list2 = []
    n = 0
    rev_str = ""
    for item in my_str:
        if item != " ":
            rev_str = rev_str + item
    rev_str = rev_str[::-1]
    for item in my_list:
        list2.append(rev_str[n:n + len(item)])
        n += len(item)
    return " ".join(list2)


print("the reverse string is ---> {}".format(reverse_str(my_str)))
