# Solution(Python)

## Recrusive

1.  If `left>right`,  the subtree is empty and the empty node is returned.

2. Select the first node of the pre-order traversal as the root node.

3. Based on pre-order traversal logic, recursive left subtree creation and right subtree creation.

## Iterative

1. Initially the stack holds the root node (the first node of the preorder traversal), with a pointer to the first node of the inorder traversal.

2. Enumerate each node in the forward traversal in turn, except for the first node.

- If index happens to point to the top of the stack, then we keep popping the top node and moving index to the right, and use the current node as the right child of the last node popped.

- if index is different from the top of the stack node, we treat the current node as the left child of the top of the stack node.

3. Add the current node to the stack.
