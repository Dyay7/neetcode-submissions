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
    
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            sell = prices[i] + dp[i+1][True]
            skip = dp[i+1][False]
            dp[i][0] = max(sell, skip)

            buy = -prices[i] + dp[i+1][False]
            skip = dp[i+1][True]
            dp[i][1] = max(buy, skip)

        return dp[0][1]
    
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            sell = prices[i] + dp[i+1][True]
            skip = dp[i+1][False]
            dp[i][0] = max(sell, skip)

            buy = -prices[i] + dp[i+1][False]
            skip = dp[i+1][True]
            dp[i][1] = max(buy, skip)

        return dp[0][1]
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next_buy = next_sell = 0
        cur_buy = cur_sell = 0

        for i in range(len(prices)-1, -1, -1):
            cur_buy = max(next_buy, -prices[i] + next_sell)
            cur_sell = max(next_sell, prices[i] + next_buy)

            next_buy = cur_buy
            next_sell = cur_sell
        return cur_buy

    # Greedy
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit 
    




    
