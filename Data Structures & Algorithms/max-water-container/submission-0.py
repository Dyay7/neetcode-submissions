class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        # amount of water -> (r - l) * min(heights[l], heights[r])
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return res
