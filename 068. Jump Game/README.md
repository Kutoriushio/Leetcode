# Solution(Pyhton)

## TC(O(N)) SC(O(1))

1. Traverse the list, record the farthest position we can get.

2. If current position `i` is smaller than `farthest`, we can use `nums[i] + i` update `farthest`.

3. If `farthest` is longer than the length of list, return `True`.