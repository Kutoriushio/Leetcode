# Solutino(Python)

## Recrusive (TC(O(N)) SC(O(N)))

1. Store the result of the inorder traversal in a list.

2. Every time when call the `next` function, pop one element from the head of the list.

## Iterative (TC(O(1)) SC(O(N)))

1. Store the root and its left child node in a stack.

2. When calling the `next` function, pop the last element of the stack, and then store its right child node in the stack.
