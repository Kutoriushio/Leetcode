# Solution(Python)

1. Initialize the boundaries of the search space as left = 0 and right = `x`.
2. We find the middle index `mid = (left + right) / 2` and compare the square of middle value with `x`:
- If the square of middle value  = `x`, return mid.
- If the square of middle value < `x`, let left = mid + 1 and repeat step 2.
- If the square of middle value > `x`, let right = mid - 1 and repeat step 2.
3. We finish the loop without finding target, return -1.
