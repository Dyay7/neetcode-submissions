class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1 # dp[0] = { 0: 1 }

        for i in range(n):
            for total, count in dp[i].items():

                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count
        return dp[n][target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] is a dictionary:
        #   key   = a possible sum after using the first i numbers
        #   value = number of ways to reach that sum
        #
        # We create n+1 dictionaries: dp[0], dp[1], ..., dp[n]
        dp = [defaultdict(int) for _ in range(n + 1)]

        # Base case:
        # Before using any numbers, the only achievable sum is 0,
        # and there is exactly 1 way to achieve it (choose nothing).
        dp[0][0] = 1

        # Build the DP table one number at a time.
        for i in range(n):
            # For every sum we could make using the first i numbers...
            for total, count in dp[i].items():

                # Option 1: assign a '+' sign to nums[i]
                # This creates a new sum: total + nums[i]
                # And we add 'count' ways because every way to make 'total'
                # becomes a way to make 'total + nums[i]' by adding nums[i].
                dp[i + 1][total + nums[i]] += count

                # Option 2: assign a '-' sign to nums[i]
                # This creates a new sum: total - nums[i]
                # Again, we add 'count' ways for the same reason.
                dp[i + 1][total - nums[i]] += count

                # for example after first iteration dp[1] = { 1: 1, -1: 1 } for [1, 1, 2]
                # and dp[2] = {2: 1,0: 2,-2: 1} after second iteration and we need dp[3]

        # After processing all n numbers, dp[n] contains:
        #   sum → number of ways to reach that sum using all numbers.
        #
        # We return how many ways reach the target sum.
        return dp[n][target]
