class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # Helper to safely add a cell to the BFS queue
        def addCell(r, c):
            # Reject out-of-bounds, visited, walls (-1)
            if (min(r, c) < 0 or r == ROWS or c == COLS or 
                (r, c) in visit or grid[r][c] == -1):
                return
            
            # Mark as visited and push into BFS queue
            visit.add((r, c))
            q.append([r, c])

        # STEP 1: Add ALL gates (value = 0) to the queue first
        # This makes BFS start from every gate simultaneously
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])     # enqueue gate
                    visit.add((r, c))    # mark visited

        # BFS distance counter — represents how far we are from a gate
        dist = 0

        # STEP 2: Multi-source BFS
        # Each BFS "layer" corresponds to distance = dist
        while q:
            # Process all nodes currently in the queue (one BFS layer)
            for i in range(len(q)):
                r, c = q.popleft()

                # Set the distance for this cell
                grid[r][c] = dist

                # Expand to 4-directional neighbors
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            # After finishing one full BFS layer, increase distance
            dist += 1