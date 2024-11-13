T = int(input())

def check():
    print(sorted(ht.keys(),reverse= True))
    for key in sorted(ht.keys()):
        if ht[key] % 2 == 1:
            return "Yes"
        else:
            continue
    return "No"
            
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    ht = {}
    for num in arr:
        if num in ht:
            ht[num] += 1
        else:
            ht[num] = 1

    print(check())
