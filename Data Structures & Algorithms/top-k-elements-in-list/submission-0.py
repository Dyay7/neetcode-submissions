class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # the index will be the count, and we will store the numbers which have that frequency
        # it is len(nums) + 1 because in the case every value is 1 for example, if the len is 5
        # then we would need index 5, if we use len(nums) that gives 0, 1, 2, 3, 4; that's why we add +1
        freq = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        


        