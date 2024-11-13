from typing import List 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for word in strs:
            s = tuple(sorted(word))
            anagrams_map[s].append(word)
        res = []
        for words in anagrams_map.values():
            res.append(words)
        return res
        
        
s = Solution
str = ["eat","tea","tan","ate","nat","bat"]
res =  s.groupAnagrams(s,str)
print(res)