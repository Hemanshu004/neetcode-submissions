# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def dfs(root,val):
            if not root:
                return TreeNode(val)
            
            if root.val>=val:
                if root.left:
                    dfs(root.left,val)
                else:
                    root.left=TreeNode(val,None,None)
                
            elif root.val<val:
                if root.right:
                    dfs(root.right,val)
                else:
                    root.right=TreeNode(val,None,None)
            return root

        return dfs(root,val)


