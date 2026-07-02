# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=0
        self.count=1
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            if self.count==k:
                self.res=root.val
            self.count+=1
            dfs(root.right)
            return self.res
        return dfs(root)

