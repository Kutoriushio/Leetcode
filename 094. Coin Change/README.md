# Solution(Python)

## TC(S*N) SC(O(S))

We think in bottom-up manner. Before calculating `dp[i]`, we have to compute all minimum counts for amounts up to `i`. On each iteration `i` of the algorithm `cost` is computed as.

`cost = min(dp[i-coin]+1, cost)`