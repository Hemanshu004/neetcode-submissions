# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1

        pos=count-n
        if pos == 0:
            return head.next
        cur=head
        count1=0
        while cur and count1<pos-1:
            cur=cur.next
            count1 +=1

        cur.next=cur.next.next
        return head



            