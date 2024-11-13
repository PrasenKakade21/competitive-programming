class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i] == " " and res != 0):
                return res
            elif(s[i] != " "):
                print(s[i])
                res += 1
        return res
    
    
sol = Solution()
s = " ,"
print(Solution.lengthOfLastWord(sol,s))