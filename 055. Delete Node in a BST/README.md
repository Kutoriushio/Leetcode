# Solution(Pyhton) (TC(O(N)) SC(O(N)))

1. If the target node has no child, we can simply remove the node.

2. If the target node has one child, we can use its child to replace itself.

3. If the target node has two children, replace the node with its in-order successor or predecessor node and delete that node.
