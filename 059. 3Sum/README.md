# Solution(Python)

## TC(O(N^2)) SC(O(1))

1. Sort the `nums`, and fix a number `i` , two pointers `left` and `right` point two ends of `nums` after index `i`, i.e.`(i+1, len(nums)-1)`

2. Calculate the sum of three nums, `nums[i] + nums[left] + nums[right]`

- If `sum < 0`, move left pointer to right by one.

- If `sum > 0`, move right pointer to left by one.

- If `sum == 0`, two pointers move by one respectively.

- Each time, if the pointers has moved, need to jump repeating elements.

- If `nums[i] > 0`, which means the numbers after index `i` all bigger than 0, return result.