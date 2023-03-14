# Solution(Python)

## Backtracking TC(O(4^N/SQRT(N))) SC(O(4^N/SQRT(N)))

1. Add `(` and `)` when we know it will remain a valid sequence.

2. Keep track of the number of opening and closing brackets we have placed so far

3. Start an opening bracket if we still have one (of `n`) left to place.

4. Start a closing bracket if it would not exceed the number of opening brackets.