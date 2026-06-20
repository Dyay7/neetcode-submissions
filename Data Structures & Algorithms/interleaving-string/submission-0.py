class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # If lengths don't match, impossible to interleave
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] = True if s1[i:] and s2[j:] can form s3[i+j:]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Base case:
        # If we've consumed all of s1 and all of s2,
        # then we've also consumed all of s3.
        dp[len(s1)][len(s2)] = True

        # Fill the table bottom‑up (from the end of the strings backwards)
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                # OPTION 1: Take next char from s1
                # Only valid if:
                #   - i is still inside s1
                #   - s1[i] matches the next needed char in s3
                #   - the rest of the suffix works (dp[i+1][j] is True)
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True

                # OPTION 2: Take next char from s2
                # Same logic as above, but for s2
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        # Final answer: can s1[0:] and s2[0:] form s3[0:]?
        return dp[0][0]