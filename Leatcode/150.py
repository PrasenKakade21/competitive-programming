from typing import List 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            #<------ a/b is wrong as we are going from top to bottom ie last to first ------->
            add = 0
            if t == '+':
                a = nums.pop()
                b = nums.pop()
                add = b+a
                nums.append(int(add))

            elif t == '-':
                a = nums.pop()
                b = nums.pop()
                add = b-a
                nums.append(int(add))

            elif t == '*':
                a = nums.pop()
                b = nums.pop()
                add = b*a
                nums.append(int(add))

            elif t == '/':
                a = nums.pop()
                b = nums.pop()
                add =int(b/a)    
                nums.append(int(add))

            else:
                nums.append(int(t))
            
        return nums.pop()
                    