class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s1 = len(haystack)
        s2 = len(needle)
        if haystack == needle:
            return 0
        for i in range(0,s1-s2):
            print(i)
            if haystack[i:i+s2] == needle:
                return i
        print(i)
        return -1
      
      
      
s = "abc"
print(s[2:3])