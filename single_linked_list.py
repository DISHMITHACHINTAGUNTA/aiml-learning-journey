class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while temp:
            temp = self.head
            while temp:
                print(temp.data ,end=" ")
                temp=temp.next
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def deleteDuplicates(self, head) :
        temp = head
        while (temp and temp.next):
            if (temp.data == temp.next.data):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
    def node_beg(self,data):
        nb=ListNode(data)
        nb.next=self.head
        self.head=nb
    def node_end(self,data):
        temp=self.head
        while True:
            if (temp.next)!=None:
                temp=temp.next
                continue
            else:
                ne = ListNode(data)
                temp.next=ne
                ne.next=None
                break
    def del_end(self):
        prev=self.head
        curr=self.head.next
        while curr.next:
            prev=prev.next
            curr=curr.next
        prev.next=None

    def del_fir(self):
        temp=self.head
        temp.next=None
        head = temp.next




n1=ListNode(10)
n2=ListNode(20)
n1.next=n2
n3=ListNode(30)
n2.next=n3
n4=ListNode(40)
n3.next=n4
n5=ListNode(40)
n4.next=n5
s=Solution()
s.head=n1
# s.display()
# print()
# s.reverse()
# s.display()
print()
s.deleteDuplicates(n1)
s.display()
n6=23
print()
# s.node_beg(n6)
# s.display()
n7=50
#s.node_end(n7)
s.del_fir()
s.display()





