# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            
            q=deque([root])
            res=[]
            j=0
            while q:
                res.append([])
                for i in range(len(q)):
                    node=q.popleft()
                    res[j].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                j+=1
            return res
        return bfs(root)