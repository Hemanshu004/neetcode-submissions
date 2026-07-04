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
        curr=head
        old={}
        while curr:
            copy=Node(curr.val)
            old[curr]=copy
            curr=curr.next
        
        cur=head
        while cur:
            copy=old[cur]
            copy.next=old[cur.next] if cur.next else None
            copy.random=old[cur.random] if cur.random else None
            cur=cur.next
        return old[head]


