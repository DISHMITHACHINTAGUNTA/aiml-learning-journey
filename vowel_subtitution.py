# input: abeaicaidao
#o/p: a
#
# st=input()
# d={}
# for i in st:
#     if i in 'aeiouAEIOU':
#         d[i]=st.count(i)
# ma=max(d.values())
# for p,q in d.items():
#     if q==ma:
#         print(p)
#         break
#
#
#
# s=input()
# d={}
# v="aeiou"
# for p in s:
#     if p in v:
#         if p not in d:
#             d[p]=1
#         else:
#             d[p]=d[p]+1
# m=max(d.values())
# for p,q in d.items():
#     if q==m:
#         print(p)
#         break

# frequent_character_replaced
#
# s=input()
# d={}#{'l':2,
# cha=input()
# for i in s:#liril
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# m=max(d.values())
# l=[]
# for p,q in d.items():
#     if q==m:
#         l.append(p)
# l.sort()
# r=s.replace(l[0],cha)
# print(r)

text=input("enter any series name :")
vowels='aeiou'
result=''
for i in text:
    if i in vowels:
        ch=(vowels.index(i)+1)%len(vowels)
        result=result+vowels[ch]
    else:
        result=result+i
print(result)