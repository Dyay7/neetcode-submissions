class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo , hi = -1, len(nums) - 1 # min problem, invalid lo valid hi

        while lo + 1 < hi:
            mid = lo + (hi - lo)//2

            if self.isOnRight(nums, mid):
                hi = mid
            else:
                lo = mid
        return nums[hi]

    def isOnRight(self, nums, index):
        return nums[index] <= nums[len(nums)-1]

"""
Turns out, we can. For a rotated sorted array, we can compare each element with the last element of the array. 
If the current value is less than or equal to the last value, then we know that we are on the right side 
of the pivot, where the condition is True. If the current value is greater than the last value, 
then we know that we are on the left side of the pivot.
"""
