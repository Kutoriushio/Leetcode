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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if size > i + 1:
                    node.next = queue[0]
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

# Solutino2
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        while cur:
            pre = Node()
            dummy = pre
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummy.next
        return root