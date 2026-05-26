# SQUARE PATTERN
a=4
for i in range(a-1):
    print("@"*a)

#right angle tringle
for i in range(1,6):
    print("!"*i)

a=8
for i in range(1,a+1):
    for j in range(1,i+1):
        print("7",end=" ")
    print()

# inverted right angle triangle

for i in range(10,0,-1):
    print("&"*i)

for i in range(10,0,-1):
    for j in range(1,i+1):
        print("9",end=" ")
    print()