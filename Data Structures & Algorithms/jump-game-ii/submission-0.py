class Solution:
    def jump(self, nums: List[int]) -> int:
        # Number of jumps taken so far.
        res = 0

        # l and r define the current "window" of indices reachable
        # with exactly 'res' jumps.
        l = r = 0

        # We stop when the right boundary reaches or passes the last index.
        while r < len(nums) - 1:

            # farthest = the maximum index we can reach with res+1 jumps.
            farthest = 0

            # Explore all indices in the current window [l, r].
            # These are all positions reachable with exactly 'res' jumps.
            for i in range(l, r + 1):
                # From index i, we can reach i + nums[i].
                # Track the farthest reachable index among all of them.
                farthest = max(farthest, i + nums[i])

            # Move the window to the next layer:
            # All indices from r+1 to farthest are reachable with res+1 jumps.
            l = r + 1
            r = farthest

            # We used one more jump to reach this new window.
            res += 1

        return res
