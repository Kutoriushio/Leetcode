# Solution(Python)

1. Initialize `length` euqals to `len(digits) - 1` 
    
2. Iterate from the end of the list.

3. Check if the last number equals to 9 or not.

4. If so, convert 9 to 0, then pointer moves to the left, and iterate until not equal to 9.

5. Check if `length < 0`.

6. If so, add 1 to the top of `digits`, otherwise add 1 to `digits[length]`.
