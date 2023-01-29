# Solution(Python)

## Solution1 (TC:O(N), SC:O(N))

Use level order traversal

## Solution2 & Solution3 (TC:O(N), SC:O(1))

1. The first case is the connection of two child nodes of the same parent node. They can be accessed directly through the same node, so the connection is completed by performing the operation `node.left.next = node.right`.

2. The second case establishes a connection between child nodes of different fathers, in which case no direct connection is possible.
- If root's next node is not null, `node.right.next = node.next.left`
- Else move to next level.

## Solution4 (TC:O(N), SC:O(1))

1. Let root's left node move to right, root's right node move to left, and then connect them.