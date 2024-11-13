from typing import List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            r = i+1
            l = len(nums)
            while(r<l):
                if nums[i]+nums[r]+nums[l] == 0:
                    res.append([i,r,l])
                elif nums[i]+nums[r]+nums[l] > 0:
                    l = l-1
                elif nums[i]+nums[r]+nums[l] < 0:
                    r = r + 1               
        return res  
        
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# -4 -1 -1 0 1 2