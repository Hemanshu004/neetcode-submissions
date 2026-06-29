# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,maxsofar):
            nonlocal count
            if not root:
                return 
            
            if root.val>=maxsofar:
                maxsofar=root.val
                count+=1
            
            if root.left:
                dfs(root.left,maxsofar)
            if root.right:
                dfs(root.right,maxsofar)
            return count
        return dfs(root,root.val)
        
        