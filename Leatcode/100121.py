from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        counter = 0
        for word in words:
            
            for c in word:
                if c == x:
                    res.append(counter)
                    break
            counter+=1
        return res