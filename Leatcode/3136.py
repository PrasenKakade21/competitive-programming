# https://leetcode.com/problems/valid-word/


class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        v = ['a','e','i','o','u']
        c = "qwrtypsdfghjklzxcvbnm"
        n = "0123456789qwertyuiopasdfghjklzxcvbnm"
        vpass = False
        cpass = False
        alnum = False
        if(len(word)<3):
            return False
        if word.isalnum():
            alnum = True
        for ch in word:
            if ch in v:
                vpass = True
            if ch in c:
                cpass = True
            if alnum == False and ch not in n:
                return False
        if(vpass and cpass):
            return True
        else:
            return False