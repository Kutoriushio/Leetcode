# Solution(Python)

## DP TC(O(N^2)) SC(O(N))

`dp[i] = max(dp[j]+1, dp[i])`, `dp[i]` means the length of the longest subsequence ending in `nums[i]`.

## Binary Search + Greedy TC(O(NlogN)) SC(O(N))

- Let's run that example `nums = [2, 6, 8, 3, 4, 5, 1]`
1. Let pick the first element, sub = [2].
2. 6 is greater than previous number, `sub = [2, 6]`
3. 8 is greater than previous number, `sub = [2, 6, 8]`
4. 3 is less than previous number, so we can't extend the subsequence sub. We need to find the smallest number >= 3 in sub, it's 6. Then we overwrite it, now `sub = [2, 3, 8]`.
5. 4 is less than previous number, so we can't extend the subsequence sub. We overwrite 8 by 4, so `sub = [2, 3, 4]`.
6. 5 is greater than previous number, `sub = [2, 3, 4, 5]`.
7. 1 is less than previous number, so we can't extend the subsequence sub. We overwrite 2 by 1, so `sub = [1, 3, 4, 5]`.
8. Finally, length of longest increase subsequence = `len(sub) = 4`.