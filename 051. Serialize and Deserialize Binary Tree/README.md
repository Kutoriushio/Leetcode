# Solution(Python) (TC(O(N)) SC(O(N)))

## Serialize

1. Use preorder traversal

2. Transfer integer to string, and store them in the list.

3. Add a comma after each value.

## Deserialize

1. Split `data` by comma.

2. Recursive traversal, create left and right subtrees.

3. If `data.pop == 'None`, means empty tree.