# Solution(Python)

1. Use HashMap to store occurrences of elements in the `nums1` array.
2. Iterate `number` in `nums2` array, check if `number` is in dictionary and `dic[number] > 0` then append `number` to our answer and decrease `dic[number]` by one.
3. To optimize the space, we ensure `len(nums1) <= len(nums2)` by swapping `nums1` with `nums2` if `len(nums1) > len(nums2)`.