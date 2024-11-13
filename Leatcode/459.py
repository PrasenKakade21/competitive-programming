# 459. Repeated Substring Pattern

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         for i in range (2,len(s) -1):
#             for j in range(i,len(s)-1):
#                 print(s[0:i] ,s[j:j+i])
#                 if(s[0:i] == s[j:j+i]):
#                     return True
#         return False
    

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(1,int(len(s)/2)+1):
            repcount = 1
            maxrep = int(len(s)/i)
            for j in range(i,len(s)):
                if(s[0:i] == s[j:j+i]):
                    repcount+=1
            print(repcount,maxrep,s[0:i])
            if(repcount == maxrep and len(s)%i == 0):
                return True
        return False
            

str = "abab"
sol = Solution()
bo = Solution.repeatedSubstringPattern(sol,str)
print(bo)