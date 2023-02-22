# Solution(Python)

## TC(O(N)) SC(O(1))

1. Quick sort `nums`, get the partition index.

- If `index = target`, it means we find the Kth largest number, return it.

- If `index < target`, we need to quick sort the right part of `nums`.

- If `index > target`, we need to quick sort the left part of `nums`.