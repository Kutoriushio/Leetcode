# Solution(Python)

## Heap TC(O(K * logK)) SC(O(K))

1. Start the pointers to point to the beginning of each rows.

2. Iterate k times, for each time `ith`, the top of the `pq` is the ith smallest element in the matrix.

3. Pop the top from the `pq` then add the next element which has the same row with that top to the `pq`.


## Binary Search TC(O(Nlog(left-right))) SC(O(1))

1. Start with `left = minOfMatrix = matrix[0][0]` and `right = maxOfMatrix = matrix[n-1][n-1]`.

2. Find the `mid` of the `left` and the `right`. This middle number is NOT necessarily an element in the matrix.

3. If `countMid(mid) >= k`, we keep current  `ans = mid` and try to find smaller value by searching in the left side. Otherwise, we search in the right side.

4. Since ans is the smallest value which `countMid(mid) >= k`, so it's the `k th` smallest element in the matrix.