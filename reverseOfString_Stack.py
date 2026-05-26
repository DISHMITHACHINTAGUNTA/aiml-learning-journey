
# l=list(map(int,input().split()))
# s=[]
# for p in range(len(l)//2):
#     s.append(l.pop())
# l.pop()
# while s:
#     l.append(s.pop())
# print(l)

#Reverse of a string using stack
#mpmc-->cmpm[append,pop,display]
st=input()
l=[]
for i  in st:
    l.append(i)
# for k in range(len(l)-1,-1,-1):
#     print(l[k],end="")
r=''
while l:
    r=r+l.pop()
print(r)