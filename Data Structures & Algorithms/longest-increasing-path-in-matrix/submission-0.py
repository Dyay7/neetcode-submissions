class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        memo = [[0 for i in range(cols)] for i in range(rows)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            # return the length of the longest increasing path starting from cell (r, c)
            if memo[r][c] != 0:
                return memo[r][c]
            best = 1
            # we explore all 4 directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Move only if the next cell is strictly larger
                    if matrix[nr][nc] > matrix[r][c]:
                        best = max(best, 1+dfs(nr, nc))
            # Save result before returning
            memo[r][c] = best
            return best

        # Try every cell as a starting point
        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))
        return answer