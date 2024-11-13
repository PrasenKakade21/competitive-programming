from typing import List
import math
class Solution:
    
    def canSortArray(self, nums: List[int]) -> bool:
        lens = []
        
        flag = True
        for num in nums:
            x=num.bit_count()
            lens.append(x)
        maxi = lens[0]
        changecount = 0
        for n in lens:
            changecount = changecount + 1
            if maxi < n:
                maxi = n
                changecount = 0 
            if(n < maxi and (changecount == 1)):
                flag = False
        print(lens)
        x = lens
        return flag

x = [8,4,2,30,15]
x = [1,2,3,4,5,8]
x = [3,16,8,4,2]
s = Solution
print(Solution.canSortArray(s,x))