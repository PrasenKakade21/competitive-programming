arr = str(input())
x = 0
ht = {}
for i in range(len(arr)):
    ht[i] = x
    if(arr[i] == "("):
        x = x + 1
    else:
        x = x - 1
print("bef",ht)
ht = dict(sorted(ht.items(), key=lambda item: item[1]))
def sorts():
    p1 = 0
    p2 = len(arr)-1
    for i in range(len(arr)):
        
        
print("aft",ht)

res = ""
for i in range(len(arr)):
    res = res + arr[ht[i]]
    
print(res)