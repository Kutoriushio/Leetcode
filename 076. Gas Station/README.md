# Solution(Python)

## TC(O(N)) SC(O(1))

1. Traverse lists, record the sum of `gas - cost`.

2. Calculate every station's rest gas.

3. If the rest gas is smaller than 0, then `[0, i]` can not be the start.