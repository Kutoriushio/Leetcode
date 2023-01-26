# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            if node == None:
                return res
            # Visit root first, then the left subtree, then the right subtree.
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)
        return res

# Iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        # Note that we add node's right child to the stack first.
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        
        return res
# Morris Traversal：
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        curr = root
        
        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree. 
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right
                    
                # If the last node is not modified, we let 
                # 'curr' be its right child. Otherwise, it means we 
                # have finished visiting the entire left subtree.
                if not last.right:
                    answer.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
        
        return answer