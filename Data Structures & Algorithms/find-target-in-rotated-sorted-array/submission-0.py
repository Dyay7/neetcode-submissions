class Solution:
    def search(self, nums, target):
        min_index = self.find_min(nums)

        if self.is_on_right(nums, target):
            return self.binary_search(nums, target, min_index, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, min_index - 1)

    def is_on_right(self, nums, target):
        return target <= nums[-1]

    # Minimization binary search:
    # Find first index i in [left, right] such that nums[i] >= target
    def binary_search(self, nums, target, left, right):
        lo = left - 1
        hi = right

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid

        return hi if nums[hi] == target else -1

    # Standard pivot finder (min element index)
    def find_min(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo