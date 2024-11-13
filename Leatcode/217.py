from typing import List 
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = defaultdict(int)
        for num in nums:
            mydict[num] = mydict[num] + 1
            if mydict[num] > 1:
                return True
        return False
            