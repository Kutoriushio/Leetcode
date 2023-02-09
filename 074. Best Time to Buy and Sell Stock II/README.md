# Solution(Python)

## Solution1 (TC(O(N)) SC(O(1)))

1. Travese the list, if the day after is lower than the current price, sold the stock.

2. Otherwise, caluculate the largest profit.

## Solution2 (TC(O(N)) SC(O(1)))

1. Traverse the entire list of stock trading day prices, the strategy is to buy and sell on all up trading days (making all profits) and not to buy and sell on all down trading days (never losing money).