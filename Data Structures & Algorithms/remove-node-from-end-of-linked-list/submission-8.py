# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head = self.reverseList(head)

        p0 = None
        p1 = head
        p2 = head.next

        while n > 1:
            
            p0 = p1
            p1 = p2
            p2 = p2.next

            n-=1

        if p0:
            p0.next = p2
        elif p2:
            head = p2
        else:
            return None
            
        return self.reverseList(head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linkedList
        last = None
        curr = head

        while curr.next:
            nxt = curr.next

            curr.next = last
            last = curr
            curr = nxt
        
        curr.next = last

        return curr

            
        