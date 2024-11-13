from typing import List
from collections import defaultdict
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        mydict = defaultdict(int)
        res = defaultdict(int)
        result = []
        for emp in access_times:
            mydict.setdefault(emp[0],[])
            mydict[emp[0]].append((int)(emp[1]))
            
        for name in mydict:
            vals = sorted(mydict[name])
            if len(vals) <= 2:
                continue

            for i in range(len(vals)-2):
                tempvals = vals[i:i+3]
                mini = min(tempvals)
                rang = (int(mini/100)+1)*100 + abs(mini%100 -1)
                print(tempvals,rang)
                t = 0
                for val in tempvals:
                    if val <= rang:
                        t += 1
                if t >= 3:
                    res[name] += 3
        for r in res:
            if res[r] >=3:
                result.append(r)
 
        return result

s = Solution
access_times = [["akuhmu","0454"],["aywtqh","0523"],["akuhmu","0518"],["ihhkc","0439"],["ihhkc","0508"],["akuhmu","0529"],["aywtqh","0530"],["aywtqh","0419"]]
s.findHighAccessEmployees(s,access_times)