from typing import List
class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        l = 0
        r = n-1
        maxVol = 0
        for _ in range(n):
            vol = min(h[l],h[r])*abs(l-r)
            if h[l]>h[r]:
                r+=1
            else:
                l+=1
            vol = max(vol,maxVol)
        return maxVol
            
            
        