class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for num in nums:
            # duplicate values cancel out x^x = 0 and unique values remains, x^0 = x
            answer ^=num
        return answer