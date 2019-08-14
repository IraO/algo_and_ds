class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
    
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
    
    def search(self, val: int) -> TreeNode:
        if not root:
            return None
        
        if val < root.val:
            return self.search(root.left, val)
        elif val > root.val:
            return self.search(root.right, val)
        else:
            return root
