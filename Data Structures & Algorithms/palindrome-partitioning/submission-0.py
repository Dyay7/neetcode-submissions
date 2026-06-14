class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            # If we've consumed the whole string, record the current partition
            if i == len(s):
                res.append(part.copy())
                return

            # Try all possible substrings starting at index i
            for j in range(i, len(s)):
                # Only continue if s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])   # choose
                    dfs(j+1)                # explore
                    part.pop()              # un-choose (backtrack)

        dfs(0)
        return res


    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True