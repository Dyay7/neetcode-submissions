class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            difference = target - nums[i]
            if numMap.get(difference, None) is not None:
                return [numMap[difference], i]
            else:
                numMap[num] = i
