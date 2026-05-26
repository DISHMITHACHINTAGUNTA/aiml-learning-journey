st="Python is super easy"
temp=[]
s=""
for i in st:
     if i !=" ":
         s+=i
     else:
        temp.insert(0,s)
        s=""
temp.insert(0,s)
reversed=" ".join(temp)
print(reversed)


a=input("Enter a string:")
lar=-1
st=""
for i in a:
    if i.isdigit():
        st+=i
    else:
        if st!="":
            if int(st)>lar:
                lar=int(st)
                st=""
print(lar)

