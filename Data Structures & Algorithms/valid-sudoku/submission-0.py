class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                ## While r < 3 -> squares(0, 0) for c < 3, squares(0, 1) for 3 <= c > 6 and squares(0, 2) for 6 <= c > 9
                squares[(r//3, c//3)].add(board[r][c])
        return True