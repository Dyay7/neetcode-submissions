class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()  # sorting is optional but keeps things consistent

        # dp[i][a] = number of ways to make amount 'a' using coins from index i onward
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case:
        # There is exactly 1 way to make amount 0: choose no coins.
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill the table bottom-up.
        # We go from the last coin backwards because dp[i] depends on dp[i+1].
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):

                # First choice: SKIP this coin.
                # If we skip coin[i], we move to the next coin (i+1)
                dp[i][a] = dp[i + 1][a]

                # Second choice: USE this coin (only if it fits in the amount).
                if a >= coins[i]:
                    # If we use coin[i], we stay at the same coin index (i)
                    # because coins can be used unlimited times.
                    #
                    # dp[i][a - coins[i]] = number of ways to make the remaining amount
                    # after using one coin[i].
                    #
                    # We ADD these ways because every way to make (a - coin[i])
                    # becomes a valid way to make 'a' by adding coin[i].
                    dp[i][a] += dp[i][a - coins[i]]

        # The answer is: number of ways to make 'amount' using all coins starting at index 0.
        return dp[0][amount]
