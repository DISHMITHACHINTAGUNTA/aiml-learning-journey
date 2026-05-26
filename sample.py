n=int(input("enter a number :"))
sum_digits=0
for i in range(1,n+1):
    if i==n:
        print(i,end="=")
    else:
        print(i,end="+")
    sum_digits += i
print(sum_digits)

st="dishu"
for i in st:
    print(i,"=",ord(i))


size=int(input("enter the size of array: ")) #7
li=list(map(int,input().split()))[:size]
print(li)





