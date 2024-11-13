from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        for i in range(len(heights)):
            if(len(heights)<2 or i == len(heights)-1):
                res.append(heights[i])
            else:
                res.append(min(heights[i],heights[i+1])*2)

        return max(res)