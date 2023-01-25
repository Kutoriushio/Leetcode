
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Traversal with Valid Range
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if node == None:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return(helper(node.left, low, node.val) and helper(node.right, node.val, high))
        
        return helper(root, -math.inf, math.inf)


# Recursive Inorder Traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node == None:
                return True
            if not inorder(node.left): # check left node 
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return inorder(node.right)

        self.pre = -math.inf
        return inorder(root)

# Iterative Inorder Traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        pre = -math.inf
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        
        return True