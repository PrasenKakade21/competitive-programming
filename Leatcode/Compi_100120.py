from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        maxXOR = 0
        
        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    currentXOR = nums[i] ^ nums[j]
                    maxXOR = max(maxXOR,currentXOR)
        return maxXOR