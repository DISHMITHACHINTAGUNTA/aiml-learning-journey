
#
#
# import math
# # independent sublist
# ind_l=[[] for k in range(5)] # create 5 DISTINCT lists , tht it creates a new empty list for every iteration
# ind_l[3].append(7)
# ind_l[0].append(23/6) # division : gives coefficient in float points
# ind_l[1].append(23//6)  # floor division : gives coefficient in whole integer points
# ind_l[2].append(23%6) # modulus : gives the remainder
# ind_l[4].append(round(math.sqrt(17),3))  # round(): gives whole integer number , sqrt() : gives square root value in float points
# print(ind_l)

#
# rounded=[]
# for inner in ind_l:     # this for loop without temp will change a nested list into 1D LIST
#     for x in inner:
#         rounded.append(round(x, 2))
# print(rounded)
#
# rounded2=[]
# for inner in ind_l:
#     temp=[]
#     for x in inner:
#         temp.append(round(x, 2))
#     rounded2.append(temp)
# print(rounded2)
# # different id for every list
# print(id(ind_l[0]), id(ind_l[1]), id(ind_l[2]), id(ind_l[3]), id(ind_l[4]))


n=input("enter a name:").strip()
print("Too long to show" if len(n)>20 else ("short enough",n))