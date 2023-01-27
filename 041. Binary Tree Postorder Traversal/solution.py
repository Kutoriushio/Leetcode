# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recrusive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right == None or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

# Iterative
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # check if right node has tarversaled or not
            if root.right == None or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res
                