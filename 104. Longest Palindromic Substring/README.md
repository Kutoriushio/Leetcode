# Solution(Python)

## Dynamic Programming TC(O(N^2)) SC(O(N^2))

1. Fill the diagonal with True, because every single character by itself is palindrom.

2. Iterate over different substring lengths.

3. If `s[i] == s[j]`

- If the length of substring equals to 2, `dp[i][j] = True` 

- Otherwise, if `dp[i+1][j-1] = True`, `dp[i][j] = True` 

## Expand Around Center TC(O(N^2)) SC(O(1))

1. Start from each position and expand in both directions.

2. Look to the right for a character in the same position as the current period until you encounter an inequality.

3. Exapand left and right in both directions until left and right are not equal.
