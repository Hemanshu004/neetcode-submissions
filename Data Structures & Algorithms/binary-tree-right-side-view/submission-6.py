# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            
            q=deque([root])
            res=[]
            while q:
                rightside=None
                for i in range(len(q)):
                    node=q.popleft()
                    if node:
                        rightside=node
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                res.append(rightside.val)
            return res
        return bfs(root)
