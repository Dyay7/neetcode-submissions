class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, max(piles) + 1   # hi must be valid, lo must be invalid

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.canFinishInHours(piles, mid, h):
                hi = mid
            else:
                lo = mid

        return hi

    def canFinishInHours(self, piles, k, h):
        if k == 0:
            return False  # avoid division by zero

        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
            if time > h:
                return False
        return True
