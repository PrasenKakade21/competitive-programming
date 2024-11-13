from collections import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = {}
        res = []
        for i in range(len(nums)):
            arr[nums[i]].append(i)
        
        for num in range(len(nums)):
            if -(num) in nums:
                res.append(num)
        
        return max(res)