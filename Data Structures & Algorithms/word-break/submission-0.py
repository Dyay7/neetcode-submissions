class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)] # this means s[i:] can be fully segmented into words
                if dp[i]: # if we find one word that matches we can skip the rest
                    break
        return dp[0]