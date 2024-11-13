from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def recursion(open:int,close:int,s : list):
            
            if(open<n):
                s.append('(')
                recursion(open+1,close,s)
                s.pop()
            if(close<n and close<open):
                s.append(')')
                recursion(open,close+1,s)
                s.pop()
            if(open==close==n):
                res.append("".join(s))
        recursion(0,0,stack)
        return res                       