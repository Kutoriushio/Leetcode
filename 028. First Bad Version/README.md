# Solution(Python)

1. Initialize the boundaries of the search space as `left = 1` and `right = n`.
2. If there are bad versions in the range `[left, right]`, we find the middle index `mid = (left + right) / 2` and compare the middle value `isBadVersion(mid)` with target:
- If`isBadVersion(mid) == False`, let `left = mid + 1` and repeat step 2.
- If `isBadVersion(mid) == True`, let `right = mid` and repeat step 2.
3. Return left or right
