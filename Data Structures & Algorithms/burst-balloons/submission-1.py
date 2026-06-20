class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends.
        # This avoids edge-case checks when bursting the first or last balloon.
        nums = [1] + nums + [1]

        # Memo dictionary: dp[(l, r)] = max coins obtainable
        # by bursting all balloons strictly inside the interval [l, r].
        dp = {}

        def dfs(l, r):
            # If the interval is empty (no balloons to burst), return 0 coins.
            if l > r:
                return 0

            # If we already computed this interval, return the cached result.
            if (l, r) in dp:
                return dp[(l, r)]

            # Initialize the best result for this interval.
            dp[(l, r)] = 0

            # Try every balloon i in the interval [l, r] as the *last* balloon to burst.
            for i in range(l, r + 1):

                # If i is the last balloon to burst in this interval,
                # its neighbors become nums[l-1] and nums[r+1].
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # Add coins from bursting the left side [l, i-1]
                # and the right side [i+1, r] independently.
                coins += dfs(l, i - 1) + dfs(i + 1, r)

                # Keep the maximum coins achievable for this interval.
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        # We start with the interval [1, len(nums)-2] because
        # the added 1's at both ends are not real balloons.
        return dfs(1, len(nums) - 2)
