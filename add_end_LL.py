class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def node_end(self, data):
        temp = self.head
        while True:
            if (temp.next) != None:
                temp = temp.next
                continue
            else:
                ne = ListNode(data)
                temp.next = ne
                ne.next = None
                break

n1=ListNode(1)
n2=ListNode(2)
n1.next=n2
n3=ListNode(3)
n2.next=n3
n4=ListNode(4)
n3.next=n4
n5=56
node_end(n5)
