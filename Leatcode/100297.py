from typing import List
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        i = 0
        j = 1 if(len(skills) > 1) else 0
        win = 0
        while(win < k):
            
            if(skills[i] > skills[j]):
               win+=1
               if win == k:
                   return i
               j+=1
            else:
                win+=1
                if win == k:
                    return i

                i = j
                
        
        res = dict(sorted(wins.items(), key=lambda item: item[1]))        
                    
                    
            # elif(skills[i] > skills[j]):
            #     if(j == i -1):
            #         j = j+2
            #     else:
            #         j = j+1
                    