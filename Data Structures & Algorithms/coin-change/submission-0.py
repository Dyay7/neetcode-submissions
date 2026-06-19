class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] will store the minimum number of coins needed to make amount 'a'
        # We initialize every value to amount+1, which acts like "infinity"
        # because the worst case is using 'amount' coins of value 1.
        dp = [amount + 1] * (amount + 1)

        # Base case: to make amount 0, we need 0 coins.
        dp[0] = 0

        # Build the solution for every amount from 1 to 'amount'
        for a in range(1, amount + 1):

            # Try every coin and see if we can use it to build amount 'a'
            for c in coins:

                # If coin c can fit into amount a (i.e., a - c is non-negative)
                if a - c >= 0:
                    # Option 1: don't use coin c → dp[a] stays the same
                    # Option 2: use coin c → 1 coin + best way to make (a - c)
                    # We take the minimum of these two options.
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still amount+1, it means we never found a valid combination
        return dp[amount] if dp[amount] != amount + 1 else -1
