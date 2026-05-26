# num=[1,5,6,4,4,7]
# sec_lowest=sorted(num)
# print(sec_lowest)
# print("second lowest number",sec_lowest[1])

s1=input("enter a string:")
cnt=1
gl=0
for i in range(len(s1)-1):
    if s1[i]==s1[i+1]:
        cnt+=1
    else:
        if cnt%2==0:
            gl+=cnt
        cnt=1
if cnt%2==0:
    gl+=cnt
print(gl)