from typing import List
from collections import defaultdict
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        mydict = defaultdict(int)
        for i in range(0,n):
            mydict[i] = 0
        for c in edges:
            mydict[c[1]] += 1
        res = {}
        s = 0
        for x in range(0,n):
            if mydict[x] == 0:
                res[s] = 0
                s +=1
        if len(res) > 1:
            return -1
        else:
            return res[0]
