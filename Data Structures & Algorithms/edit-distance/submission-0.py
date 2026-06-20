class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] will store the minimum number of operations needed
        # to convert word1[i:] into word2[j:]
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # BASE CASE 1:
        # If word1 is empty (i == len(word1)), the only way to match word2[j:]
        # is to INSERT all remaining characters of word2.
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # BASE CASE 2:
        # If word2 is empty (j == len(word2)), the only way to match word1[i:]
        # is to DELETE all remaining characters of word1.
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Fill the DP table bottom‑up.
        # We go backwards so that dp[i+1][j], dp[i][j+1], dp[i+1][j+1]
        # are already computed when we need them.
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # If characters match, no operation is needed.
                # We simply move diagonally to the next pair.
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    # Otherwise, we consider the three possible operations:
                    # 1. Delete word1[i]      → dp[i+1][j]
                    # 2. Insert word2[j]      → dp[i][j+1]
                    # 3. Replace word1[i]     → dp[i+1][j+1]
                    # We take the minimum and add 1 for the operation we perform.
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],     # delete
                        dp[i][j + 1],     # insert
                        dp[i + 1][j + 1]  # replace
                    )

        # dp[0][0] contains the answer for converting the full word1 → word2.
        return dp[0][0]
