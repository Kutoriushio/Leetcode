class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            cost = math.inf
            for coin in coins:
                if i - coin >= 0:
                    cost = min(dp[i-coin]+1, cost)
            dp[i] = cost
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]