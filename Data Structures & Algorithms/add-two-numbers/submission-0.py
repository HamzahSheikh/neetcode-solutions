# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()

        curr = ans
        c1 = l1
        c2 = l2

        carry = 0

        while l1 or l2 or carry == 1:

            curr.next = ListNode()
            curr = curr.next
            
            a = 0
            b = 0

            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + carry
            carry = 0

            if total > 9:
                total = total%10
                carry = 1
            
            curr.val = total
            

        return ans.next
            

            
        