"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Recursive:
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def helper(node, res):
            if node is None:
                return res
            res.append(node.val)
            for child in node.children:
                helper(child,res)
            return res
        result = []
        return helper(root, result)


# Iterative:
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        result = []
        stack = [root]

        while stack:
            temp = stack.pop()
            result.append(temp.val)

            if temp.children != None:
                stack.extend(temp.children[::-1])
        
        return result