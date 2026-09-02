class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = set()
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]  # l means the next position where I should place a new unique value
                l += 1
        return l