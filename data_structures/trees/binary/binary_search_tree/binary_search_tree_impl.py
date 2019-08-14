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

    def search(TreeNode, val: int) -> TreeNode:
        if not self.root:
            return None
        curr = self.root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None
     
    def search_recursively(self, val: int) -> TreeNode:
        if not root:
            return None
        
        if val < root.val:
            return self.search(root.left, val)
        elif val > root.val:
            return self.search(root.right, val)
        else:
            return root

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val <= root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            else:
                root.val = self.minVal(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root
    
    def minVal(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val
