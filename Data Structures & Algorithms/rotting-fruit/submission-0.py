class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()   # queue for BFS (stores rotten oranges)
        fresh = 0                 # count of fresh oranges
        time = 0                  # minutes passed

        # STEP 1: Count fresh oranges and enqueue all rotten ones
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1            # count fresh oranges
                if grid[r][c] == 2:
                    q.append((r, c))      # multi-source BFS: start from ALL rotten oranges

        # 4-directional movement
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # STEP 2: BFS — spread rot minute by minute
        # Continue only while there are fresh oranges AND rotten ones to spread infection
        while fresh > 0 and q:
            length = len(q)   # number of rotten oranges for this minute (one BFS layer)

            # Process all oranges that rot others in the current minute
            for i in range(length):
                r, c = q.popleft()

                # Try to rot all 4 neighbors
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Check bounds and ensure the neighbor is a fresh orange
                    if (row in range(len(grid)) and 
                        col in range(len(grid[0])) and 
                        grid[row][col] == 1):

                        grid[row][col] = 2      # rot the fresh orange
                        q.append((row, col))    # it will rot others next minute
                        fresh -= 1              # one less fresh orange

            # After processing one full BFS layer, one minute has passed
            time += 1

        # If no fresh oranges remain, return time; otherwise impossible → return -1
        return time if fresh == 0 else -1
