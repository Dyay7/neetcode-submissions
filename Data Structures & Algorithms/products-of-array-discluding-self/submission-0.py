class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        # let's say we have [1,2,3,4]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # prefix would be [1, 1, 2, 6], each index corresponds to the preceding multiplication for nums[i+1]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        # postfix goes from right to left, 4 doesn't have a postfix so it is 1, and then res would go like
        # [24, 12, 4, 1]
        return res

        # Time complexity would be O(n) [O(n+n)]
        # Space complexity would be O(n) since we create an array of n elements, n being len(nums)
