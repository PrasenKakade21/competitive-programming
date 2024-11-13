for T in range(int(input())):
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    res = 0
    m,n = max(l,L), min (r,R)
    
    if n-m < 0:
        if abs(n-m) < 2:
            res = 1
    elif n-m == 0:
        res == 2 
    else :
        res = n-m 

    print(res)
    