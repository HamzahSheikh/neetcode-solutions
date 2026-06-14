# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hare = head
        tortoise = head

        index = 0

        while hare != None and tortoise != None:

            if hare == tortoise and index != 0:
                return True

            tortoise = tortoise.next

            if hare.next != None:
                hare = hare.next.next
            else:
                hare = None

            index += 1

        return False
        