from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def conseg(arr):
            arr.sort() 
            n = len(arr)
            if n == 1:
                return 1
            count = 1
            maxc = -1
            for i in range(n - 1):
                if arr[i + 1] - arr[i] == 1:
                    count += 1
                elif arr[i + 1] - arr[i] == 0:
                    continue
                else:
                    count = 1 
                maxc = max(maxc, count)
            return maxc

        res = min(conseg(hBars),conseg(vBars))+1
        return res*res
                
            
        
        