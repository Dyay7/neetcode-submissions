class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0

        for two in range(len(nums)):
            tmp = nums[two]
            nums[two] = 2
            if tmp < 2:
                nums[one] = 1
                one += 1
            if tmp < 1:
                nums[zero] = 0
                zero += 1