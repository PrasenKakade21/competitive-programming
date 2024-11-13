from typing import List 
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        res = []
        for num in nums:
            mydict[num] += 1
        
        s = sorted(mydict.values(),reverse=True)[k-1]
        print(s)
        
        for num in mydict:
            if mydict[num] < s:
                continue
            else:
                res.append(num)
        return res
    
nums = [1,1,1,3,2,2]
k = 2
s = Solution
print(s.topKFrequent(s,nums,k))