# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        queue = deque()

        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next

        first = True

        dummy = ListNode()
        curr = dummy

        while queue:

            if first:
                curr.next = queue.popleft()
                first = False
            else:
                curr.next = queue.pop()
                first = True

            curr = curr.next

        curr.next = None