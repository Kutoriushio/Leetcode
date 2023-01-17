# Solution(Python)

1. Start both indexes `(index, i)` from 1.

2. Check if the previous element `nums[i-1]` is different from the current element `nums[i]`.

3. If found different then make `nums[index] = nums[i]` and increment `index` by 1.

4. Increment `i` by 1 till end of the `nums`.