from typing import List 
from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_prefix = [nums[0]]
        product_suffix = [nums[n-1]]
        res = []
        for i in range(1,n):
            product_prefix.append(product_prefix[i-1] * nums[i])
            product_suffix.append(product_suffix[i-1] * nums[n-i-1])
        for i in range(0,n):
            if i == 0:
                res.append(product_suffix[n-i-2])
                print(product_suffix[n-i-2])
   
            elif i == n-1:
                res.append(product_prefix[i-1])
                print(product_prefix[i-1])
                
            else:
                res.append(product_prefix[i-1]*product_suffix[n-i-2])
                print(i,product_prefix[i-1],product_suffix[n-2-i])
        print(product_prefix)
        print(product_suffix)
        print(res)
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        right = 1
        for i in range(0,n):
            res[i] = right 
            right *= nums[i]
        left = 1
        for i in range(n-2,-1,-1):
            res[i] *= left 
            left *= nums[i]

        return res
    
        
s = Solution
l = [4,3,2,1,2]
l =[-1,1,0,-3,3]
l = [1,2,3,4,5,4,3,2,1]

s.productExceptSelf(s,l)

# [1,2,3,4]
# [1 2 6 24]
# [24 24 12 4]
# [24,12,8,6]

# [4 12 24 24]

# [-1,1,0,-3,3]
# [-1 -1 0 0 0]
# [3 -9 0 0 0]
# [0,0,9,0,0]
