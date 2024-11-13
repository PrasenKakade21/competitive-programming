from typing import List
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        res = 0
        cp = 0
        for i in range(len(prices)):
            print(cp)
            if(i == 0):
                res += prices[0]
                cp += 2
            else:
                if( len(prices) < cp+1):
                    break
                if( len(prices) < cp+2 and prices[cp]>prices[cp+1]):
                    if(prices[cp-1]<prices[cp]):
                        res += prices[cp-1]
                        cp +=1 
                    else:
                        res += prices[cp]
                        cp+=2
                elif( len(prices) < cp+2 and prices[cp]==prices[cp+1]):
                    res = prices[cp+1]
                    cp += 3
                else:
                    res += prices[cp]
                    cp+=2
        print(res)
        return res

s = Solution()
prices = [3,1,2]
s.minimumCoins(prices)