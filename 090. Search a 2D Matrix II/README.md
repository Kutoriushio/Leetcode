# Solution(Python)

## TC(O(M+N)) SC(O(1))

1. Initialize the current position to top right corner or bootom left corner.

2. If the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted. 

3. If the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. 