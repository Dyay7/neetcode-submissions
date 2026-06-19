class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0) # where we don't choose any elements to have just a sum of 0 + value

        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                # we take every value in dp and add it to nextDP and also add t+nums[i]
                nextDP.add(t+nums[i])
                # since we will update dp as nextDP we need to add t to have it too
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False