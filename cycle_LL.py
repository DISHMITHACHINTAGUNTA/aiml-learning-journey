class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if (slow==fast):
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None



n1=ListNode(10)
n2=ListNode(20)
n1.next=n2
n3=ListNode(30)
n2.next=n3
n4=ListNode(40)
n3.next=n4
n4.next=n2
s=Solution()
s.head=n1
s.detectCycle(n1)