# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxdepth=0
        q=deque([(root,1)])
        
        while q:
            
            node,height=q.popleft()

            maxdepth=max(maxdepth,height)
            if node.left:
                q.append((node.left, height + 1))

            if node.right:
                q.append((node.right, height + 1))
        return maxdepth
