class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        # dp[i][j] is the number of ways to form t[:j] using s[:i]
        dp = [[0] * (m+1) for _ in range(n+1)]


        for i in range(n+1):
            dp[i][0] = 1

        # fill the table row by row

        for i in range(1, n+1):
            for j in range(1, m+1):
                # First option is to skip s[i-1]
                dp[i][j] = dp[i-1][j]

                # Second option is to use s[i-1], only if it matches t[j-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[n][m]
