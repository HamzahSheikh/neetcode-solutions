"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head

        copy = Node(0)
        ans = copy

        items = {}

        while curr.next:
            copy.val = curr.val

            items[curr] = copy

            copy.next = Node(0)
            copy = copy.next
            curr = curr.next

        copy.val = curr.val
        items[curr] = copy

        curr1 = head
        curr2 = ans

        while curr1:
            if curr1.random:
                curr2.random = items[curr1.random]

            curr1 = curr1.next
            curr2 = curr2.next

        return ans