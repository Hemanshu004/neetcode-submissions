# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maxsofar):
            count=0
            if not root:
                return 0
            
            if root.val>=maxsofar:
                maxsofar=root.val
                count+=1
            
            if root.left:
                count+=dfs(root.left,maxsofar)
            if root.right:
                count+=dfs(root.right,maxsofar)
            return count
        return dfs(root,root.val)
        
        