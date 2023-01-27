# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p == None and q == None:
                return True
            if not(p and q):
                return False
            if p.val != q.val:
                return False

            return (dfs(p.left, q.right) and dfs(p.right, q.left))
        
        return dfs(root.left, root.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root.left, root.right]
        while queue:
            p = queue.pop(0)
            q = queue.pop(0)
            if p == None and q == None:
                continue
            if not(p and q):
                return False
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True