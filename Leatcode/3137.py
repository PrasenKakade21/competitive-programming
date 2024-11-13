class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        ht = {}
        p1 = 0
        p2 = k
        while(p2<len(word)):
            ht[word[p1:p2]] = ht[word[p1:p2]] + 1  
            p1 = p1 + k
            p2 = p2 + k
        ht = dict(sorted(ht.items(), key=lambda item: item[1]))
        
                 