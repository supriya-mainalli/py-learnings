
def longest_subs(my_str):
    max_length = 0
    for i in range(len(my_str)):
        seen = set()
        for j in range(i, len(my_str)):
            if my_str[j] not in seen:
                seen.add(my_str[j])
                len_ = j-i+1
                max_length = max(max_length, len_)
            else:
                break
    return max_length
# print(longest_subs("bbbbb"))

def optimal_substring(my_str):
    my_dict = {}
    l = 0
    r = 0
    n = len(my_str)
    max_length = 0
    while(r<n):
        if my_str[r] in my_dict:
            if my_dict[my_str[r]]>= l:
                l = my_dict[my_str[r]] + 1
        len_ = r-l+1
        max_length = max(max_length, len_)
        my_dict[my_str[r]] = r
        r += 1
    return max_length

print(optimal_substring("pwwkew"))
    

