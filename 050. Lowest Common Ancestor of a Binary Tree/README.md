# Solution(Python)

1. Recursive left child node, return value noted as `left`.

2. Recursive right child node, return value noted as `right`.

3. Accroding to `left` and `right`, which can be explained in four cases:
- `left` and `right` equal to None, which means neither of the left/right subtrees contains `p`, `q`.
- `left` and `right` both don't equal to None, which means `p`, `q` is on the opposite side of the root.
- `left` or `right` don't equal to None, return `left` or `right`.