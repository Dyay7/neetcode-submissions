class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # If we've matched ALL characters in the word, success
            if i == len(word):
                return True

            # If out of bounds, wrong character, or already visited → fail this path
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # Temporarily mark this cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 directions for the next character
            res = (dfs(r + 1, c, i + 1) or   # down
                   dfs(r - 1, c, i + 1) or   # up
                   dfs(r, c + 1, i + 1) or   # right
                   dfs(r, c - 1, i + 1))     # left

            # Restore the cell after exploring (backtracking)
            board[r][c] = temp

            return res

        # Try starting DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # Only return True if *one* starting point works
                if dfs(r, c, 0):
                    return True

        # If no starting point works, the word doesn't exist
        return False
