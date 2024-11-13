T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    ht = {}
    for num in arr:
        if num in ht:
            ht[num] += 1
        else:
            ht[num] = 1
    
    print(n-max(ht.values()))