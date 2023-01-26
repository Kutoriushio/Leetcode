# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recrusive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res = []
        inorder(root)
        return res

# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res

# Morris Traversal:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        cur = root
        while cur:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree. 
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
            else:
                last = cur.left
                while (last.right and last.right != cur):
                    last = last.right
                # If the last node is not modified, we let 
                # 'curr' be its right child. Otherwise, it means we 
                # have finished visiting the entire left subtree.
                if last.right == None:
                    last.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    cur = cur.right

        return res