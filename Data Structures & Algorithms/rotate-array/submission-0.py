class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        while k:
            temp = nums[n-1]
            for i in range(n-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = temp
            k -= 1

        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(left, right):
            while left < right:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
                left += 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)