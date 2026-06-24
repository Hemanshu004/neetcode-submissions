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
            return 

        old={}
        curr=head
        while curr:
            copy=Node(curr.val)
            old[curr]=copy
            curr=curr.next
        
        curr=head
        while curr:
            copy=old[curr]
            copy.next=old[curr.next] if curr.next else None
            copy.random=old[curr.random] if curr.random else None
            curr=curr.next
        return old[head]
