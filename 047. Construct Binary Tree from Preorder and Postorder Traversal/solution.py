# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, post):
            if not pre:
                return None
            if len(pre) == 1:
                return TreeNode(pre[0])
            root = TreeNode(pre[0])
            count = post.index(pre[1]) + 1
            root.left = dfs(pre[1:count+1], post[:count])
            root.right = dfs(pre[count+1:], post[count:-1])
            return root
        
        return dfs(preorder, postorder)