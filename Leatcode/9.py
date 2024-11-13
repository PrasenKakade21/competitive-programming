class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = [0]
        y = x
        while y%10 >0:
            nums.append(y%10)
            y = y/10
        return nums == nums[:-1]