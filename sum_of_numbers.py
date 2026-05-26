# Addition of digits of a given number
# n=int(input("Enter a number:"))
# sum,temp=0,0
# for i in range(n):
#     sum+=1
#     if (i == n - 1):
#         print(sum ,"=",end=" ")
#     else:
#         print(sum,"+",end=" ")
#     temp+=sum
# print(temp)

# multiplication of digits of a given number
n=int(input("Enter a number:"))
sum,temp=0,1
for i in range(n):
    sum+=1
    if (i == n - 1):
        print(sum ,"=",end=" ")
    else:
        print(sum,"*",end=" ")
    temp*=sum
print(temp)