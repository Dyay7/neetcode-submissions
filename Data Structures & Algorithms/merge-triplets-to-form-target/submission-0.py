class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # at least one of the numbers in the triplet matches the target
            # and for the ones that don't they are less than the target
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3