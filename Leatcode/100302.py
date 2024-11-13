from typing import List
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        rx = [""]
        ry = [""]
        sizex = 0
        sizey = 0
        for i in range(len(points)):
            p = abs(points[i][0])
            if p > sizex and s[i] not in rx:
                size = p
                rx.append(s[i])

            elif p == sizex and s[i] in rx:
                q = rx.find(s[i])
                if abs(points[q][0]) == p:
                    rx.remove(q)
                rx.append(s[i])
                
            p = abs(points[i][1])
            if p > sizey and s[i] not in ry:
                sizey = p
                ry.append(s[i])

            elif p == sizey and s[i] in ry:
                q = ry.find(s[i])
                if abs(points[q][0]) == p:
                    ry.remove(q)
                ry.append(s[i])
        r1 = []
        r2 = []
        for r in rx:
            if r != "":
                r1.append(r)
        for r in ry:
            if r != "":
                r2.append(r)
        print(rx)
        print(ry)
        print(sizex)
        print(sizey)
        return min(len(rx)-1,len(ry)-1)