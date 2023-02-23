# Solution(Python)

## Solution1 TC(O(N)) SC(O(N))

1. Use `prefix` to store every number's product of prefix.

2. Use `suffix` to store every number's product of suffix.

3. Every number's `prefix * suffix` is the result.


## Solution2 TC(O(N)) SC(O(1))

1. First cycle to calculate every number's product of prefix.

2. Second cycle to calculate every number's product of suffix.

## Optimize Solution TC(O(N)) SC(O(1))

1. One cycle to calculate every number's product of prefix and suffix.