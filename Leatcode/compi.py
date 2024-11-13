from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        j = 1
        i = 0
        for num in range(0,n):
            if j > len(grid[i]):
                
            if grid[i][j] == 0:
                i = j
                j+=1
            else:
                j+=1
        return i
                
                

s = Solution
grid = [[0,0,1],[1,0,1],[0,0,0]]
x = s.findChampion(s,grid)
print(x)