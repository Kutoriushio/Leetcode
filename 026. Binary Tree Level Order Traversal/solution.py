# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            cur_level = []
            next_level = []
            for node in queue:
                cur_level.append(node.val)               
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(cur_level)
            queue = next_level
        
        return res

# DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(depth, node):
            if node is None:
                return
            
            if len(result) < depth:
                result.append([])
            
            result[depth-1].append(node.val)

            if node.left:
                dfs(depth+1, node.left)
            if node.right:
                dfs(depth+1, node.right)
        
        dfs(1, root)
        return result
            