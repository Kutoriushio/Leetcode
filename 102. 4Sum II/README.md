# Solution(Python)

## TC(O(N^2)) SC(O(N^2))
1. Divide given lists into two groups and precalculating all possible sums for the first group.

2. Results go to a hashmap where keys are sums and values are frequencies.

3. Iterate over elements of the second group, and for every pair check whether their sum can add up to zero with a sum from the first group using a hashmap.