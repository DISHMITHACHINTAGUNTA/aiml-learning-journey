l=[[]]*3
l[0].append(1)
print(l)
# ALL 3 ELEMENTS SHARE SAME LIST
print(id(l[0]), id(l[1]), id(l[2]))
l[2].append(5)
print(l)
l[1].remove(1)
print(l)



chars=['a','a','a','f','f','g','g','g']
li = []
c = 1
for i in range(len(chars) - 1):
    if chars[i] == chars[i + 1]:
        c += 1
    else:
        li.append(chars[i])
        if c > 1:
            li.extend(str(c))
        c = 1
li.append(chars[-1])
if c > 1:
    li.extend(str(c))
chars[:] = li
print(chars,len(chars))