class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        substr = []
        for str in word:
            if (len(substr) == 3):
                
                for i in range(len(substr)):
                    