# Solution(Python)

## Backtracking TC(O(N×N!)) SC(O(1))

1. Boolean arrays `used`, all initialised with `false` to indicate that the numbers have not been selected, are set to `true` when we select a number.

2. When we select enough numbers, end the recrusion.

3. Then we need to revoke last selection.

4. Backtracking will clear the state, so we need append the copy of `path`.