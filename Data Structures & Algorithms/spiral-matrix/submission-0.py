class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # Boundaries of the current layer of the spiral
        left, right = 0, len(matrix[0])          # horizontal boundaries
        top, bottom = 0, len(matrix)             # vertical boundaries

        # Continue while there is still a valid rectangle to traverse
        while left < right and top < bottom:

            # 1. Traverse the top row from left → right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1   # shrink the top boundary (we consumed that row)

            # 2. Traverse the right column from top → bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # shrink the right boundary

            # If boundaries crossed, stop (prevents double-counting in odd shapes)
            if not (left < right and top < bottom):
                break

            # 3. Traverse the bottom row from right → left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # shrink the bottom boundary

            # 4. Traverse the left column from bottom → top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # shrink the left boundary

        return res
