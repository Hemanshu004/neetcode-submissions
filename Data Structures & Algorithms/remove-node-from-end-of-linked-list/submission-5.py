# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=dummy
        while n>0:
            curr=curr.next
            n-=1
        
        while curr.next:
            curr=curr.next
            prev=prev.next
        
        tmp=prev.next.next
        prev.next.next=None
        prev.next=tmp
        return dummy.next


