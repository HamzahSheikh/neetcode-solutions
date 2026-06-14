# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        
        hare = head.next
        tortoise = head

        while hare != None and tortoise != None:

            if hare == tortoise:
                return True

            tortoise = tortoise.next

            if hare.next != None:
                hare = hare.next.next
            else:
                return False


        return False
        