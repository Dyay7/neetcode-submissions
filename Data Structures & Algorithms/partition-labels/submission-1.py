class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i # we set the last index for each character
        
        res = []

        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            # in each character, we check end, because if one has a higher end than the previous one
            # it needs to be updated, else it stays the same

            if i == end:
                res.append(size)
                size = 0
        return res
