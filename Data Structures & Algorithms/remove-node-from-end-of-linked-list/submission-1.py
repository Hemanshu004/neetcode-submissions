# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        i=0
        while curr:
            i+=1
            curr=curr.next
        
        idx=(i-n)
        if idx==0:
            return head.next
        prev=None
        node=head
        for _ in range(idx):
            prev=node
            node=node.next
        
        prev.next=node.next
        return head
       