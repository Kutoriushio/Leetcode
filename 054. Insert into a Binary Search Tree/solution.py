# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if node.val > val:
                # if the left subtree of node is empty, insert into its left side.
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                # if the right subtree of node is empty, insert into its right side.
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root

# Recrusive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root