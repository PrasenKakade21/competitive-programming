from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = nums[0]
        end = 0
        res = []
        for i in range(len(nums)-1):
            if(nums[i+1] == nums[i]+1):
                end = end + 1
            elif end < start:
                res.append(start)
            else:
                res.append(str(start) + "->" + str(end))
                start = nums[i+1]
        return res
                
        