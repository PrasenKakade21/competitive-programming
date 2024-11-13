from typing import List 
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        
        for i in range(len(grid[0])-1):
            if grid[0][i] == grid[0][i+1]:
                return False
        for i in range(len(grid)-1):
            if grid[i] != grid[i+1]:
                return False
        return True

s = Solution()
grid = [[1,1,2],[1,1,2]]
# grid = [[1,1,1],[0,0,0]]
b = s.satisfiesConditions(grid)
print(b)