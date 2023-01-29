"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Solution1
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if size - 1 > i:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

# Solution2
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        
        return root

# Solution3
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root

# Solution4
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if not root:
                return root
            left = root.left
            right = root.right
            while left:
                left.next = right
                left = left.right
                right = right.left
            dfs(root.left)
            dfs(root.right)

            return root
        
        return dfs(root)