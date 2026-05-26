n=int(input("enter the size of array:"))
if n<=0:
    print(-1)
else:
    l = list(map(int, input().split()))[:n]
    r=[]
    r.append(l[-1])
    for p in range(0,len(l)-1):
        d=max(l[p+1:])
        if l[p]>d:
            r.append(l[p])
    if n>0:
        print(sum(r))
    else:
        print("-1")