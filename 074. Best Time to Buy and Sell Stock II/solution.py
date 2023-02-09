class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit1 = 0
        profit2 = 0
        buy = math.inf
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            temp = prices[i] - buy
            if i < len(prices) - 1:
                if prices[i+1] < prices[i]:
                    profit1 += temp
                    buy = math.inf
                    profit2 = 0
                    continue
            profit2 = max(temp, profit2)
        return profit1 + profit2
    

    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            res = 0
            for i in range(1, len(prices)):
                if prices[i-1] < prices[i]:
                    diff = prices[i] - prices[i-1]
                    res += diff
        
        return res