class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # def rob(self, nums: List[int]) -> int:
    #     memo = [-1] * len(nums)

    #     def dfs(i):
    #         if i >= len(nums):
    #             return 0

    #         if memo[i] != -1:
    #             return memo[i]

    #         memo[i] = max(
    #             dfs(i + 1),           # skip house i
    #             nums[i] + dfs(i + 2)  # rob house i
    #         )

    #         return memo[i]

    #     return dfs(0)