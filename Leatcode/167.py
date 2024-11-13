from typing import List
class Solution:
    def twoSum1(self, nums: List[int], t: int) -> List[int]:
        n = len(nums)
        a = int(n/2 - 1)
        b = int(n/2) 
        c = 0
        adds = nums[a]+nums[b]
        while(adds != t):
            if(adds > t):
                if a > 0:
                    a -=1
                else:
                    b -= 1
                    
            elif adds<t:
                if b < n-1:
                    b+=1
                else:
                    a+=1
            c +=1
            adds = nums[a] + nums[b]
        print(c)
        return [a+1,b+1]
    
    
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l,r = 0,len(nums)-1
        c = 0
        while l<r:
            s = nums[l] + nums[r]
            c +=1
            if s > t:
                r -= 1
            elif s < t: 
                l +=1
            else :
                print(c)
                return [l+1,r+1]
            
numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
t = 542

s = Solution

print(s.twoSum1(s,numbers,t))
