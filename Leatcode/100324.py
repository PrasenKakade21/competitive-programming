class Solution:
    def clearDigits(self, s: str) -> str:
        arr = list(s)
        closestalpha = []
        for i in range(len(arr)):
            a = str(arr[i])
            if(a.isnumeric() and closestalpha != []):
                arr[i] = ""
                arr[closestalpha[len(closestalpha)-1]] = ""
                closestalpha.pop()
            else:
                closestalpha.append(i)
                
            print(arr,closestalpha)
        res = ""
        for cha in arr:
            if(cha != ""):
                res += cha
        print(res)
        return res




s = Solution()
s.clearDigits("b4y6sdg46fh5")