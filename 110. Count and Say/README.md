# Solution(Python)

## Iterative TC(O(N)) SC(O(1))

1. Keep track of the first letter in the sequence and count consecutive occurances.

2. Once you encounter a new letter you add the previous count and letter to the chain.

3. Repeat n-1 times (since we seeded the initial '1' case). 

4. We always update temp after the inner loop since we will never have already added the last sequence.

## Recrusive TC(O(N)) SC(O(1))

1. The same as the iterative.