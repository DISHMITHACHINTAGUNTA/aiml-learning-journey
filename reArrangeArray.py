# n=int(input("enter size :"))
# l=list(map(int,input().split()))[:n]
# l.sort()
# p1=0
# p2=len(l)-1
# r=[]
# while p1<p2:
#     r.extend([l[p1],l[p2]])
#     p1=p1+1
#     p2=p2-1
# if len(l)%2!=0 :
#     r.append(l[p1])
# print(*r) # print in string


#frquency of each element (using array or dict)
#l=[1,2,3,4,5,1,2] -->0(n)
# HINT: use ascii values of num to reduce time complexity


l=list(map(int,input().split()))#1 2 3 4 5 1 2
# d={}#{1:2,2:2,3:1,4:1,5:1}
# for p in l:
#     d[p]=l.count(p)
# print(d)   #o(n^2)

f=[0]*256
for p in range(len(l)):
    f[ord(str(l[p]))]=f[ord(str(l[p]))]+1
for p in range(len(f)):
    if f[p]>0:
        print(chr(p),f[p])    #o(n)





