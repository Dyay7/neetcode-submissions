class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if self.canFinishInHours(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def canFinishInHours(self, piles, k, h):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
            if time > h:
                return False
        return True
