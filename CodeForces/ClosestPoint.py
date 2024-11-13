for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    if n == 2:
        if abs(arr[0] -arr[1]) > 1:
            print("YES")
    else:
        print("NO")
        
