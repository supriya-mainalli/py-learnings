class Solution:
    def containsNearbyDuplicate(nums, k):
        result = {}
        new_list = []
        for i in range(len(nums)):
            if result.get(nums[i]) == None:
                result[nums[i]] = new_list + [i]
            else:
                result[nums[i]].append(i)
        for val in result.values():
            if len(val) > 1:
                print(val)
                for i in range(len(val) - 1):
                    for j in range(i + 1, len(val)):
                        print(val[i], val[j])
                        if val[j] - val[i] <= k:
                            return True
        return False


print(Solution.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
