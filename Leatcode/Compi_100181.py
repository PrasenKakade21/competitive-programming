from collections import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minsum =  nums[0]
        nums[0] = max(nums)
        x = nums
        for _ in range(2):
            min = max(nums)
            minInd = 0
            for i in range(len(nums)):
                if(x[i] < min):
                    min = x[i]
                    minInd = i
            minsum = minsum + min
            x[minInd] = max(nums)+1
        return minsum
        
        
        
        
        
        
        
1 2 3 12