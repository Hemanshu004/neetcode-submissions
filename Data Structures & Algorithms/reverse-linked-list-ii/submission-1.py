# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        dummy=ListNode(0,head)
        leftprev=dummy
        for _ in range(left-1):
            leftprev,curr=curr,curr.next
        
        prev=None
        for _ in range(right-left+1):
            tmp1=curr.next
            curr.next=prev
            prev=curr
            curr=tmp1   
        
        leftprev.next.next=curr
        leftprev.next=prev
        return dummy.next 

