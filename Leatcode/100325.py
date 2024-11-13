class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        x =  (k+1) % n 
        bounce = int(k/n)
        y = k % n
        print(bounce,y,x)
        if bounce % 2 == 0 or bounce == 0:
            return y
        else:
            return n - y 
        
          