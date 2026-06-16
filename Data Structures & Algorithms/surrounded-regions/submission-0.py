class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # STEP 1: BFS from border 'O's to mark all SAFE regions
        # Any 'O' connected to the border cannot be captured.
        def capture():
            q = deque()

            # Add all border 'O's to the queue
            for r in range(ROWS):
                for c in range(COLS):
                    # Check if cell is on the border AND is 'O'
                    if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r, c))

            # BFS flood-fill from all border 'O's
            while q:
                r, c = q.popleft()

                # Only process if still 'O'
                if board[r][c] == "O":
                    board[r][c] = "T"   # Mark as TEMPORARILY SAFE

                    # Explore all 4 neighbors
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        # If neighbor is inside bounds, add to queue
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            if board[nr][nc] == "O":
                                q.append((nr, nc))

        # Mark all border-connected 'O's as 'T'
        capture()

        # STEP 2: Flip the board
        for r in range(ROWS):
            for c in range(COLS):

                # Any 'O' NOT connected to border is surrounded → flip to 'X'
                if board[r][c] == "O":
                    board[r][c] = "X"

                # Any 'T' was safe → restore back to 'O'
                elif board[r][c] == "T":
                    board[r][c] = "O"