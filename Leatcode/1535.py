from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        wincount = 0
        opp = 1
        while(wincount < k):
            if opp > n-1:
                break
            if arr[0] > arr[opp]:
                wincount += 1     
            elif arr[0] < arr[opp]:
                arr[0],arr[opp] = arr[opp],arr[0]
                wincount = 1          
            opp += 1
        return arr[0]