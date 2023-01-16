# Solution(Python):

1. Calculate the sum of `nums` as `s`.
2. The sum to the left of index `i` is `leftsum`, then to the right of index will be `s - leftsum - nums[i]`.
3. Initialize `leftsum` with `0`
4. Iterate every index, check whether `leftsum` euqals to `s - leftsum - nums[i]`, and maintain the correct value of `leftsum`.