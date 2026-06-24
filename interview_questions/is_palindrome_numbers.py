class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = x
        rev_num = 0
        i = 0
        if x<=0:
            return False
        while(i<nums):
            digit = nums%10
            rev_num = rev_num*10+digit
            nums = nums//10
            i += 1
        print(rev_num)

s = Solution()
s.isPalindrome(1234)
        