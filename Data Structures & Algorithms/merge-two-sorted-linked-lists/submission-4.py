# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        q1=list1
        q2=list2
        while q1 and q2:
            if q1.val>q2.val:
                curr.next=q2
                q2=q2.next
            else:
                curr.next=q1
                q1=q1.next
            curr=curr.next
        if q1:
            curr.next=q1
        if q2:
            curr.next=q2
        return dummy.next
