# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):        
            if not root:
                return [0,0]
            leftpairs=dfs(root.left)
            rightpairs=dfs(root.right)
            withRoot=root.val+leftpairs[1]+rightpairs[1]
            withoutRoot=max(leftpairs)+max(rightpairs)
            
            return[withRoot,withoutRoot]
        return max(dfs(root))