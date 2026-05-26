size=int(input("enter size of queue"))
q=[]
front=-1
rare=-1
def enqueue():
    global front,rare
    if rare <size-1 :
        if front==-1:
            front=0
        rare=rare+1
        ele=int(input("enter ele"))
        q.append(ele)
    else:
        print("the top ele is:",q[0])
def display():
    if front==-1:
        print("Queue is empty")
    else:
        print(*q)
def peek():
    if front==-1:
        print("Queue is empty")
    else:
        print("the top ele is:", q[0])
def dequeue():
    global front,rare
    if front==-1:
        print("Queue is empty")
    elif front!=rare:
        print("the deleted ele is:",q.pop(0))
        front=front+1
    else:
        print("the deleted ele is :",q.pop(0))
        front=-1
        rare=-1
print("Queue operations:")
while True:
    print("1.Enqueue,2.Dequeue,3.Display,4.peek")
    opt=int(input("enter your option:"))
    match opt:
        case 1:enqueue()
        case 2:dequeue()
        case 3:display()
        case 4:peek()
        case 5:break
        case _:print("invalid option")
