# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        Right=head
        for _ in range(right):
            Right=Right.next
        
        Left=dummy
        for _ in range(left-1):
            Left=Left.next
        
        curr=Left.next
        prev=None
        while curr!=Right:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        
        Left.next.next=Right
        Left.next=prev

        return dummy.next








