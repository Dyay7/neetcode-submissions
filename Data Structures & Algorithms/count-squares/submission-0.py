class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for (px, py), diagonal_count in self.point_count.items():
            if px == x or py == y:
                continue
            
            if abs(px-x) != abs(py-y):
                continue
            
            corner1 = (x, py)
            corner2 = (px, y)

            squares += (diagonal_count * self.point_count.get(corner1, 0)* self.point_count.get(corner2, 0))
        return squares