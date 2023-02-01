# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC(O(N)) SC(O(N))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if abs(left - right) > 1:
                self.res = False
            return max(left, right)+1
        
        depth(root)
        return self.res

# TC(O(N)) SC(O(N))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1: # if subtree isn't balanced, the tree is also unbalanced.
                return -1
            else:
                return max(left, right)+1
        
        return depth(root) >= 0