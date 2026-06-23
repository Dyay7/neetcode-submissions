class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        answer = n

        for i in range(n):
            answer ^= i
            answer ^= nums[i]
        
        return answer