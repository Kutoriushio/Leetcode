# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        queue1 = [root]
        queue2 = [root.val]
        while queue1:
            node = queue1.pop(0)
            s = queue2.pop(0)
            if node.left == None and node.right == None:
                if s == targetSum:
                    return True
            if node.left:
                queue1.append(node.left)
                queue2.append(s+node.left.val)
            if node.right:
                queue1.append(node.right)
                queue2.append(s+node.right.val)
        
        return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetSum - root.val == 0
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)