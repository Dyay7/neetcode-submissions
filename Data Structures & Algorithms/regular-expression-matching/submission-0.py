class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # Memo: cache[(i, j)] stores whether s[i:] matches p[j:]
        cache = {}

        def dfs(i, j):
            # If we've consumed the entire pattern,
            # the match is valid only if we've also consumed the entire string.
            if j == n:
                return i == m

            # Return cached result if already computed.
            if (i, j) in cache:
                return cache[(i, j)]

            # Check if current characters match:
            # - s[i] must exist
            # - and either characters are equal OR pattern has '.'
            match = i < m and (s[i] == p[j] or p[j] == ".")

            # CASE 1: Next pattern char is '*'
            # p[j] + '*' means:
            #   - skip the "x*" entirely → dfs(i, j+2)
            #   - OR if current chars match, consume one char of s → dfs(i+1, j)
            if (j + 1) < n and p[j + 1] == "*":
                cache[(i, j)] = (
                    dfs(i, j + 2) or        # skip "x*"
                    (match and dfs(i + 1, j))  # use "x*" to match one char of s
                )
                return cache[(i, j)]

            # CASE 2: No '*', but characters match normally
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # CASE 3: Characters don't match and no '*'
            cache[(i, j)] = False
            return False

        # Start matching from the beginning of both strings.
        return dfs(0, 0)
