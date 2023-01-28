# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            index = dic[val]
            root = TreeNode(val)

            root.right = helper(index+1, right)
            root.left = helper(left, index-1)
            return root
        dic = {}
        for i, v in enumerate(inorder):
            dic[v] = i
        return helper(0, len(inorder)-1)