# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        ans = ListNode()
        curr = ans
        breakCondition = 0

        while len(lists) > breakCondition:
            
            winner = float('inf')
            winnerIndex = 0

            for i, x in enumerate(lists):

                if not x:
                    continue

                if winner > x.val:
                    winnerIndex = i
                    winner = x.val

            curr.next = ListNode(winner) 
            lists[winnerIndex] = lists[winnerIndex].next

            if not lists[winnerIndex]:
                breakCondition +=1

            curr = curr.next

        return ans.next

        

            
