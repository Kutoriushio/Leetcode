# Solution(Python)

## TC(O(N^2)) SC(O(1))

1. Transfer each element in list from int to string.

2. Sort the list by using  this equation `nums[j] + nums[j+1] < nums[j+1] + nums[j]`.

3. If the first element equals to 0, return 0.