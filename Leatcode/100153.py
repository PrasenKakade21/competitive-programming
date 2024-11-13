from typing import List
from collections import defaultdict
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        map = defaultdict(int)
        coins.sort()
        checkmap()
        
        for m in map[1:len(map)-1]:
            
        def checkmap():
            for i in range(0,len(coins)):
                subsum = 0
                for coin in coins[0:i]:
                    subsum += coin    
                map.append(subsum)
        
        