# Solution(Python)

1. Create the root node with the first element of the preorder traversal.

2. Use the second element `x` of the pre-traversal to find the corresponding index `y` in the post-traversal and add `y+1` to get the length of left subtrees.

3. Splitting the pre-order array, post-order array into left and right parts.