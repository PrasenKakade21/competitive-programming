T = int(input())

def checkN(i,j,matx):
    l,r,u,d = 0,0,0,0
    if (j+1) < len(matx[i]): 
        r =  matx[i][j+1]
 
    if (i + 1) < len(matx):
        d = matx[i+1][j]
   
  
    if j>0:
       l = matx[i][j-1] 
      

    if i>0:
        u = matx[i-1][j] 
        
    if max(l,r,u,d) < matx[i][j]:
        matx[i][j] = max(l,r,u,d)
for _ in range(T):
    n,m= map(int,input().split())
    matx = [[]*m]*n
    for i in range(n):
        
        matx[i]= list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            checkN(i,j,matx)
    for i in range(n):
        print(*(matx[i]))
