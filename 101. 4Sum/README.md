# Solution(Python)

## Two pointers TC(O(N^3)) SC(O(N))

1. Sort the array.

2. Use two loops to enumerate the first two numbers separately, then use a double pointer to enumerate the remaining two numbers after the number enumerated in the two loops.
- If the sum is equal to `target`, the four numbers enumerated are added to the answer, then the left pointer is shifted right until a different number is encountered and the right pointer is shifted left until a different number is encountered.
- If the sum is smaller than `target`, the left pointer is shifted right.
- If the sum is bigger than `target`, the right pointer is shifted left.

3. Pruning operations
- If `nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target`, it is clear that whatever the value of the remaining three numbers, the sum of the four must be greater than `target` so exit the first loop.
- If `nums[i] + nums[n-1] + nums[n-2] + nums[n-3] > target`, this means that whatever the value of the remaining three numbers, the sum of the four must be less than target, so the first loop goes directly to the next round
- The same to the second number.