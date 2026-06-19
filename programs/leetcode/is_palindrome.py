# https://leetcode.com/problems/palindrome-number/

def is_palindrome(x):
    if str(x) != str(x)[::-1]:
        return False
    return True


# print(is_palindrome(-121))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        new_res = list(filter(lambda x: x.isalpha(), s))
        new_res = ''.join(new_res)
        print(new_res)
        first = 0
        last = len(new_res)-1
        while(first<last):
            # print(s)
            if new_res[first]==new_res[last]:
                first +=1
                last -=1
            else:
                return False
        return True
s_obj = Solution()
print(s_obj.isPalindrome("0P"))

            
        
