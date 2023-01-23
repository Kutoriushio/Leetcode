# Solution(Python)

1. Initialize the boundaries of the search space as `left = 0` and `right = len(nums) - 1`.
2. If there are elements in the range `[left, right]`, we find the middle index `mid = (left + right) / 2` and compare the middle value `nums[mid]` with target:
- If `nums[mid] = target`, return `mid`.
- If` nums[mid] < target`, let `left = mid + 1` and repeat step 2.
- If `nums[mid] > target`, let `right = mid - 1` and repeat step 2.
3. We finish the loop without finding target, return -1.
