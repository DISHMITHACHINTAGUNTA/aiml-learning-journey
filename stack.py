from unittest import case
size=int(input("enter the size:"))
top=-1
s=[]
def push():
    global top
    if top <size-1:
        val=int(input("enter a value:"))
        top=top+1
        s.append(val)
    else:
        print("stack is full/overflow")
def display():
    if top!=-1:
        for p in range(len(s)-1,-1,-1):#(3,-1,-1)
            print(s[p],end=" ")#40 30 20 10
    else:
        print("stack is empty")
    print()
def peek():
    if top!=-1:
        print("top element is :",s[-1])
    else:
        print("stack is empty")
def pop():
    global top
    if top!=-1:
        print("the deleted element is:",s.pop())
        top=top-1
    else:
        print("stack is empty")

def del_mid():
    global top
    pos=size//2
    l=[]
    for i in range(pos):
        if top==-1:
            print("stack is empty")
            break
        else:
            ele=s.pop()
            l.append(ele)
            top=top-1
    s.pop()
    for i in range(len(l)-1,-1,-1):#(1,-1,-1)
        s.append(l[i])
        l.pop()
        top=top-1


print("stack operations:")
while True:
    print("1.push,2.pop,3.Display,4.peek,5.deleteMiddle")
    opt=int(input("enter your option:"))
    match opt:
        case 1:push()
        case 2:pop()
        case 3:display()
        case 4:peek()
        case 5:del_mid()
        case _:print("invalid option")


