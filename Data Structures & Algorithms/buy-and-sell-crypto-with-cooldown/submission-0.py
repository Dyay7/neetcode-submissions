class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0, 0] for _ in range(n+2)]
        #dp[i][0] -> max profit starting from day i if we are not holding a coin
        #dp[i][1] -> max profix starting from day i if we are holding a coin
        for i in range(n-1, -1, -1):
            # not holding: buy today or skip today
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i+1][0]) #buy or skip

            # holding: sell today or keep holding
            dp[i][1] = max(prices[i] + dp[i+2][0], dp[i+1][1])

        return dp[0][0]