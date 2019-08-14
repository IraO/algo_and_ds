# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root) -> List:
        res = []
        if not root:
            return res
        
        if root.left:
            res += self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self.inorder(root.right)
        return res
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        ordered_nodes = self.inorder(root)
        for i in range(1, len(ordered_nodes)):
            if ordered_nodes[i-1] >= ordered_nodes[i]:
                return False
        
        return True
