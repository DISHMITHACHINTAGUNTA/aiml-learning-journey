#l=[1,2,3,4,5]
#reverse first 3 ele in a queue-->[3,2,1,4,5]
#l=[1,2,3,4,5,6,7,8,9,10]
#reverse first k ele in queue,k=4
#[4,3,2,1,5,6,7,8,9,10]

#
# from collections import deque
# s=deque()
# n=int(input("enter size:"))
# k=int(input("enter the size to be removed:"))
# for i in range(n):
#     ele=int(input("enter element:"))
#     s.append(ele)
# l=[]
# for i in range(k):
#     p=s.popleft()
#     l.append(p)
# for j in range(len(l)):
#     s.append(l.pop())
# for g in range(len(s)):
#     s.append(s.popleft())
# print(s)


l=[1,2,3,4,5]
n=len(l)
k=3
s=[]
for p in range(k):
    s.append(l.pop(0))
while s:
    l.append(s.pop( ))
for p in range(n-k):
    l.append(l.pop(0))
print(l)