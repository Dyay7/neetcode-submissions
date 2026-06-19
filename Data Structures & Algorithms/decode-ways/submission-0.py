class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # at the end of the string there's only one possible decoding

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0 #invalid
            res = dfs(i+1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)