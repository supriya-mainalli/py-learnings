class Solution:
    def removeDuplicates(self, nums):
        seen = {}
        res = []

        for item in nums:
            seen[item] = seen.get(item, 0) + 1
            if seen[item] <= 2:
                res.append(item)
        print(res)



s = Solution()
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
    
        

               

            

               
               
