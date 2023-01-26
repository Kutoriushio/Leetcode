# Solution(Python)

## Two traversals:
1. Traversal from the root node.

2. If the current node is `p`, then the node was successfully found.

3. If the value of the current node is greater than the value of `p` means that `p` should be in the left subtree of the current node, so move the current node to its left subtree.

4. If the value of the current node is less than the value of `p` means that `p` should be in the right subtree of the current node, so move the current node to its right subtree.

5. For nodes q similarly.

6. The lowest common ancestor of `p` and `q` is the last identical node.

## One traversal:

1. Traverse from the root node.

2. if the value of the current node is greater than the values of `p` and `q`, it means that `p` and `q` should be in the left subtree of the current node, so move the current node to its left subtree.

3. if the value of the current node is less than the values of `p` and `q`, it means that `p` and `q` should be in the right subtree of the current node, so the current node is moved to its right subtree.
4. If the value of the current node does not satisfy the above two requirements, then the current node is the 'bifurcation point'. In this case, either `p` and `q` are in different subtrees of the current node, or one of them is the current node.