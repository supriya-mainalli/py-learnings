def str_compression_expansion(s):
    my_dict = {}
    res = ""
    for item in s:
        my_dict[item] = my_dict.get(item, 0) + 1
    for k,v in my_dict.items():
        res = res + k + str(v)
    return res

print(str_compression_expansion("aabbbccccddddd"))