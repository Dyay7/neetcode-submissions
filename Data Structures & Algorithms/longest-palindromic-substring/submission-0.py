class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # resIdx = starting index of the best palindrome found
#         # resLen = length of the best palindrome found
#         resIdx, resLen = 0, 0
#         n = len(s)

#         # dp[i][j] will be True if s[i:j+1] is a palindrome
#         dp = [[False] * n for _ in range(n)]

#         # Fill the DP table from bottom to top (i = n-1 → 0)
#         # because dp[i][j] depends on dp[i+1][j-1]
#         for i in range(n - 1, -1, -1):
#             # j starts from i and moves rightward
#             for j in range(i, n):

#                 # A substring s[i:j+1] is a palindrome if:
#                 # 1. The end characters match: s[i] == s[j]
#                 # 2. AND one of the following is true:
#                 #    a) The substring length is <= 3 (j - i <= 2)
#                 #       - length 1: always palindrome
#                 #       - length 2: "aa" type
#                 #       - length 3: "aba" type
#                 #    b) OR the inside substring s[i+1:j] is a palindrome
#                 if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
#                     dp[i][j] = True  # mark this substring as palindrome

#                     # If this palindrome is longer than the best so far, update result
#                     if resLen < (j - i + 1):
#                         resIdx = i
#                         resLen = j - i + 1

#         # Return the longest palindromic substring found
#         return s[resIdx : resIdx + resLen]