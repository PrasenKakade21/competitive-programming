import math

class Solution:
    prev = 0
    def climbStairs(self, n: int) -> int:
        
        return self.calc(self,n)
        
    def calc(self,n:int) ->int:
        if(n > 1):
            return Solution.climbStairs(self,n-1)+Solution.climbStairs(self,n-2)
        else:
            return 0 
        
    
        
        
        
        
        
        
        
        
# n = 1
# 1       
        
# n = 2
# 1 1
# 2

# n = 3
# 1 1 1
# 1 2
# 2 1

# n = 4
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2
