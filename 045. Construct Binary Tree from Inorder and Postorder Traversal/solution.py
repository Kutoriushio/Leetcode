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

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        n = len(postorder)-1
        val = postorder[n]
        root = TreeNode(val)
        stack = [root]
        index = n
        for i in range(1, n+1):
            node = stack[-1]
            val = postorder[n-i]
            if node.val != inorder[index]:
                node.right = TreeNode(val)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index -= 1
                node.left = TreeNode(val)
                stack.append(node.left)
        
        return root