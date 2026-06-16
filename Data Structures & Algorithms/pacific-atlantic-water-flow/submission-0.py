class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to track which cells can reach each ocean
        pac, atl = set(), set()

        # DFS that flows *uphill* (reverse of water flow)
        # We start from the oceans and move inward
        def dfs(r, c, visit, prevHeight):
            # Stop if:
            # - already visited
            # - out of bounds
            # - current height is LOWER than previous (water can't flow uphill)
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return

            # Mark this cell as reachable for the current ocean
            visit.add((r, c))

            # Continue DFS in all 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # STEP 1: Start DFS from all Pacific-bordering cells
        # Pacific touches top row and left column
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])              # top row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # bottom row (Atlantic)

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])              # left column
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # right column (Atlantic)

        # STEP 2: Any cell reachable by BOTH oceans is a valid answer
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
