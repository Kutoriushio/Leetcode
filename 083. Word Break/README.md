# Solution(Python)

## TC(O(N^3)) SC(O(N))

1. `dp[i]` indicates whether a word consisting of the letters of [0,i) of the string `s` can be concatenated with words from the dictionary.

2. For the state transfer, consider the enumeration of the partition point `j (0 <= j <= i)`, splitting the string into `[0,j)` and `[j,i)`.

3. So if `[j,i)` is in the dictionary and `dp[j]` is true , then `dp[i] = true`.