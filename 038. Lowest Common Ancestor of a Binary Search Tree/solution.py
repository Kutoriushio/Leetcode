# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Two traversals
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(root, target):
            path = []
            while root != target:
                path.append(root)
                if root.val > target.val:
                    root = root.left
                else:
                    root = root.right
            path.append(root)
            return path
        path_p = getPath(root, p)
        path_q = getPath(root, q)
        for u,v in zip(path_p, path_q):
            if u == v:
                res = u
        
        return res

# One traversal
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if (root.val < p.val and root.val < q.val):
                root = root.right
            elif (root.val > p.val and root.val > q.val):
                root = root.left
            else:
                return root