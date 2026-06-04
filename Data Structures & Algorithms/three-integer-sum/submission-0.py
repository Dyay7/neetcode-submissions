class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if a > 0: # all remaining numbers are positive because it is sorted
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            # Now it is like the two sum problem
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    # We can now move both pointers inward since the list is sorted
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result