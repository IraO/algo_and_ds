# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.ordered_nodes =  self.inorder(root)
        self.pointer = 0

        
    def inorder(self, root) -> List:
        if not root:
            return []
        res = []
        if root.left:
            res += self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self.inorder(root.right)
        return res
        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.pointer += 1
        return self.ordered_nodes[self.pointer-1]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.pointer < len(self.ordered_nodes)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
