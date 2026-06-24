# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupprev=dummy 

        while True:
            kth=self.getkth(groupprev,k)
            if not kth:
                break
            groupnext=kth.next
            prev,cur=kth.next,groupprev.next
            while cur!=groupnext:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp1=groupprev.next
            groupprev.next=kth
            groupprev=tmp1
        return dummy.next
        
    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr