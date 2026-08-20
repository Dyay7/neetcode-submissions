class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = math.ceil(len(nums) / 2)
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            if count[nums[i]] == target:
                return nums[i]
            else:
                continue
