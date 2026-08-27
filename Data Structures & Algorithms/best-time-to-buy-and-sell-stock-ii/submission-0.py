class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(prices))]

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0

            if memo[i][can_buy] is not None:
                return memo[i][can_buy]

            if can_buy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)

                memo[i][can_buy] = max(buy, skip)

            else:
                sell = prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)

                memo[i][can_buy] = max(sell, skip)

            return memo[i][can_buy]

        return dfs(0, True)
