# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root:
                data.append('None,') 
                return
            data.append('{},'.format(root.val))
            preorder(root.left)
            preorder(root.right)
        data = []
        preorder(root)
        return ''.join(data)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        data.pop()
        def dfs(data):
            node = data.pop(0)
            if node == 'None':
                return
            root = TreeNode(int(node))
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))