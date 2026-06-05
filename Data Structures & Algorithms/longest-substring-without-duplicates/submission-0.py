class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # l jumps to the right of the last occurrence of the repeated character, but never moves backward.
                # if l is behing the window we don't move it backwards, we would stay at l
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
