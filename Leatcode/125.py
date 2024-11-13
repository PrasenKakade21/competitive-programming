class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [' ','!',',']
        pure = ""
        for l in s:
            if l.isalnum():
                pure += l
        if pure == pure[:-1]:
            return True
        else:
            return False