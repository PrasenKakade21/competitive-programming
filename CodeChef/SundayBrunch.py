n=int(input())
neigh=20
if(1<=n<=405):
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        c=x//y
        if(c<=20):
            print(c)
        else:
            c=20
            print(c)